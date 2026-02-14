"""
MkDocs hooks for mind-flow blog.

Automatically extracts dates from blog post filenames and injects them
into page metadata for rendering by MkDocs Material theme.

Tags are stored in HTML comments (<!-- tags: tag1, tag2 -->) which are:
- Invisible on GitHub (clean rendering)
- Extracted by scripts/generate-tags.py to create docs/blog/tags.md
- Injected as visible HTML badges in MkDocs by this hook
"""

import re
from datetime import datetime


def on_page_markdown(markdown, page, config, files):
    """
    Extract date and tags from blog post and inject them below the title.

    Date extraction:
    - Extracts from filename pattern: blog/YYYY/YYYY-MM-DD-*.md
    - Injects published date HTML after the first heading

    Tag extraction:
    - Extracts from HTML comment on line 2: <!-- tags: tag1, tag2 -->
    - Injects as visible badge HTML after the date
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

    return markdown
