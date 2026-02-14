"""
MkDocs hooks for mind-flow blog.

Automatically extracts dates from blog post filenames and injects them
into page metadata for rendering by MkDocs Material theme.
"""

import re
from datetime import datetime


def on_page_markdown(markdown, page, config, files):
    """
    Extract date from blog post filename and inject it below the title.

    Only applies to files matching pattern: docs/blog/YYYY/YYYY-MM-DD-*.md
    Injects the published date HTML right after the first heading.
    """
    # Get the source file path
    src_path = page.file.src_path

    # Only process blog posts (not wiki or other pages)
    if not src_path.startswith('blog/'):
        return markdown

    # Skip the blog index page
    if src_path.endswith('blog/index.md'):
        return markdown

    # Extract date from filename pattern: blog/YYYY/YYYY-MM-DD-*.md
    match = re.search(r'blog/\d{4}/(\d{4}-\d{2}-\d{2})-', src_path)

    if match:
        date_str = match.group(1)

        try:
            # Parse the date
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Format as "Saturday, Feb 14, 2026"
            formatted_date = date_obj.strftime('%A, %b %d, %Y')

            # Inject the date HTML after the first heading (# Title)
            # Match the first markdown heading and insert date HTML after it
            pattern = r'^(#\s+.+)$'
            replacement = r'\1\n\n<p class="md-content__date"><small><strong>Published:</strong> ' + formatted_date + r'</small></p>'

            markdown = re.sub(pattern, replacement, markdown, count=1, flags=re.MULTILINE)

        except ValueError:
            # Invalid date format in filename - skip
            pass

    return markdown
