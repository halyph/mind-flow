#!/usr/bin/env python3
"""
Generates RSS and Atom feed files for the blog using feedgen library.

This script:
- Scans all markdown files in docs/blog/YYYY/ directories
- Extracts post metadata (title, date) from markdown files
- Reads full post content from built HTML in site/ directory
- Generates both RSS 2.0 and Atom 1.0 feeds using feedgen
- Creates feed.xml (RSS) and feed.atom (Atom) in the site directory
"""

import glob
import re
from datetime import datetime, timezone
from pathlib import Path
from feedgen.feed import FeedGenerator

# Configuration
PREFIX = 'docs/blog/'
SITE_DIR = 'site'
RSS_FILE = 'feed.xml'
ATOM_FILE = 'feed.atom'
EXCLUDE_FILES = ['index.md', 'tags.md']

# Site metadata
SITE_NAME = 'Mind~Flow'
SITE_URL = 'https://halyph.github.io/'
SITE_DESCRIPTION = 'Blog and/or personal knowledge base'
SITE_AUTHOR = 'Orest Ivasiv'
SITE_AUTHOR_EMAIL = 'halyph@gmail.com'
REPO_URL = 'https://github.com/halyph/mind-flow'
LANGUAGE = 'en'
MAX_ITEMS = 20  # Limit feed to most recent posts


def list_blog_files():
    """Find all blog post markdown files."""
    files = glob.glob(PREFIX + '**/*.md', recursive=True)
    return [f for f in files
            if '/' in f
            and not f.startswith('misc')
            and not any(f.endswith(excluded) for excluded in EXCLUDE_FILES)]


def extract_metadata(file_path):
    """Extract title, date, and URL from a blog post file.

    Returns:
        dict: Contains 'title', 'date', 'datetime', 'url', 'html_path'
    """
    # Extract date from filename (YYYY-MM-DD)
    match = re.search(r'(\d{4})/(\d{4}-\d{2}-\d{2})-(.+)\.md$', file_path)
    if not match:
        return None

    year, date_str, slug = match.groups()

    # Parse date
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    except ValueError:
        return None

    # Read title from first line
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # Remove leading # and whitespace
            title = first_line.lstrip('#').strip()
    except Exception:
        title = slug.replace('-', ' ').title()

    # Build URL and HTML path
    url = f"{SITE_URL}blog/{year}/{date_str}-{slug}/"
    html_path = Path(SITE_DIR) / 'blog' / year / f"{date_str}-{slug}" / 'index.html'

    return {
        'title': title,
        'date': date_str,
        'datetime': date_obj,
        'url': url,
        'html_path': html_path
    }


def extract_content_from_html(html_path):
    """Extract article content from built HTML file.

    Args:
        html_path: Path to the HTML file

    Returns:
        str: HTML content or empty string if not found
    """
    if not html_path.exists():
        return ''

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Extract content from <article> tag
        article_match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
        if article_match:
            return article_match.group(1)

        # Fallback: try to find main content area
        content_match = re.search(r'<div class="md-content"[^>]*>(.*?)</div>\s*</div>\s*</main>',
                                  html_content, re.DOTALL)
        if content_match:
            return content_match.group(1)

    except Exception as e:
        print(f"Warning: Could not extract content from {html_path}: {e}")

    return ''


def generate_feeds(posts):
    """Generate RSS and Atom feeds using feedgen.

    Args:
        posts: List of post metadata dicts
    """
    # Sort posts by date (newest first) and limit
    sorted_posts = sorted(posts, key=lambda p: p['datetime'], reverse=True)[:MAX_ITEMS]

    # Initialize feed generator
    fg = FeedGenerator()
    fg.id(SITE_URL)
    fg.title(SITE_NAME)
    fg.author({'name': SITE_AUTHOR, 'email': SITE_AUTHOR_EMAIL})
    fg.link(href=SITE_URL, rel='alternate')
    fg.link(href=SITE_URL + ATOM_FILE, rel='self')
    fg.subtitle(SITE_DESCRIPTION)
    fg.language(LANGUAGE)

    # Add entries
    for post in sorted_posts:
        fe = fg.add_entry()
        fe.id(post['url'])
        fe.title(post['title'])
        fe.link(href=post['url'])
        fe.published(post['datetime'])
        fe.updated(post['datetime'])
        fe.author({'name': SITE_AUTHOR, 'email': SITE_AUTHOR_EMAIL})

        # Add full content if available
        content = extract_content_from_html(post['html_path'])
        if content:
            fe.content(content, type='html')
        else:
            fe.summary(post['title'])

    return fg


def main():
    """Main entry point."""
    # Collect all blog posts
    posts = []
    for file_path in list_blog_files():
        metadata = extract_metadata(file_path)
        if metadata:
            posts.append(metadata)

    print(f"Found {len(posts)} blog posts")

    # Generate feeds
    fg = generate_feeds(posts)

    # Ensure site directory exists
    site_path = Path(SITE_DIR)
    site_path.mkdir(exist_ok=True)

    # Write RSS feed
    rss_file_path = site_path / RSS_FILE
    fg.rss_file(str(rss_file_path), pretty=True)
    print(f"Generated {rss_file_path} with {min(len(posts), MAX_ITEMS)} items")

    # Write Atom feed
    atom_file_path = site_path / ATOM_FILE
    fg.atom_file(str(atom_file_path), pretty=True)
    print(f"Generated {atom_file_path} with {min(len(posts), MAX_ITEMS)} items")


if __name__ == "__main__":
    main()
