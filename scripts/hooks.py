"""
MkDocs hooks for mind-flow blog.

This hook performs three transformations on blog posts during the build:

1. **Date Extraction**: Extracts publication date from filename pattern (YYYY-MM-DD)
   and injects it as HTML metadata below the title.

2. **Tag Processing**: Extracts tags from HTML comments (<!-- tags: tag1, tag2 -->)
   and injects them as clickable badge links in the rendered post.
   - Tags are invisible on GitHub (clean markdown rendering)
   - Extracted by scripts/generate-tags.py to create docs/tags/index.md
   - Transformed to clickable links by this hook in MkDocs

3. **Thumbnail Transformation**: Converts markdown images with alt text "thumbnail"
   to floating right-aligned HTML divs.
   - Source: ![thumbnail](path/to/image.ext)
   - Output: <div class="note inline end"><p><img src="filename.ext"></p></div>
   - Works for both GitHub (uses relative path) and MkDocs (extracts filename only)
   - Styled by docs/assets/css/extra.css
   - Toggle with ENABLE_THUMBNAIL_TRANSFORM flag

MkDocs Hook Reference:
- on_page_markdown: Called for every page before markdown->HTML conversion
  https://www.mkdocs.org/dev-guide/plugins/#on_page_markdown
"""

import re
from datetime import datetime

# ============================================================================
# Feature Flags
# ============================================================================

ENABLE_THUMBNAIL_TRANSFORM = True
"""
Toggle thumbnail transformation feature.

When True:  ![thumbnail](path/image.ext) → Floating right-aligned div
When False: ![thumbnail](path/image.ext) → Normal markdown image (no transformation)

Change this to False if you want to temporarily disable thumbnail styling
without modifying post content or CSS.
"""


def on_page_markdown(markdown, page, config, files):
    """
    Process blog posts: inject date/tags metadata and transform thumbnail images.
    See module docstring for details.
    """
    # Get the source file path
    src_path = page.file.src_path

    # Only process blog posts (not wiki or other pages)
    if not src_path.startswith('blog/'):
        return markdown

    # Skip the blog index and tags pages
    if src_path.endswith('blog/index.md') or src_path.endswith('blog/tags.md'):
        return markdown

    # === Extract tags from HTML comment ===
    tags_text = ""
    lines = markdown.split('\n')
    if len(lines) >= 2:
        # Look for HTML comment on line 2: <!-- tags: tag1, tag2 -->
        tag_match = re.search(r'<!--\s*tags:\s*(.+?)\s*-->', lines[1])

        if tag_match:
            tags_str = tag_match.group(1)
            # Split by comma, strip whitespace, lowercase
            tags = [tag.strip().lower() for tag in tags_str.split(',') if tag.strip()]

            if tags:
                # Create simple text links for tags
                tag_links = []
                for tag in tags:
                    # Link to the tags page with anchor (tags.md is at docs/tags.md)
                    tag_slug = tag.replace(' ', '-')
                    tag_links.append(f'<a href="../../../tags/#{tag_slug}">{tag}</a>')

                # Join with bullet separator: 🏷️ scala • akka • time management
                tags_list = ' • '.join(tag_links)
                tags_text = f' <span class="md-tags">• 🏷️ {tags_list}</span>'

    # === Extract date from filename ===
    date_and_tags_html = ""
    match = re.search(r'blog/\d{4}/(\d{4}-\d{2}-\d{2})-', src_path)

    if match:
        date_str = match.group(1)

        try:
            # Parse the date
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Format as "Saturday, Feb 14, 2026"
            formatted_date = date_obj.strftime('%A, %b %d, %Y')

            # Combine date and tags on same line: Published: Saturday, Jan 31, 2026 • 🏷️ git
            date_and_tags_html = f'\n\n<p class="md-content__date"><small><strong>Published:</strong> {formatted_date}{tags_text}</small></p>'

        except ValueError:
            # Invalid date format in filename - skip
            pass

    # === Inject date and tags after the title ===
    if date_and_tags_html:
        # Match the first markdown heading and insert date/tags HTML after it
        pattern = r'^(#\s+.+)$'
        replacement = r'\1' + date_and_tags_html

        markdown = re.sub(pattern, replacement, markdown, count=1, flags=re.MULTILINE)

    # === Transform thumbnail images ===
    # Convert: ![thumbnail](path/to/image.ext) → <div class="note inline end">...</div>
    # Extracts just filename for MkDocs (since it creates post/index.html in same dir as images)
    # Works for both GitHub (normal markdown) and MkDocs (floating right-aligned div)
    if ENABLE_THUMBNAIL_TRANSFORM:
        def transform_thumbnail(match):
            """Callback for re.sub() - extracts filename and wraps in floating div."""
            full_path = match.group(1)
            filename = full_path.split('/')[-1]  # Extract just filename from path
            return f'<div class="note inline end"> <p><img alt="thumbnail" src="{filename}"></p> </div>'

        # Match markdown images with alt text "thumbnail"
        markdown = re.sub(
            r'!\[thumbnail\]\(([^)]+)\)',
            transform_thumbnail,
            markdown
        )

    return markdown
