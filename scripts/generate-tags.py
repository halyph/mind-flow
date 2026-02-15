#!/usr/bin/env python3
"""
Generate docs/tags/index.md from HTML comment tags in blog posts.

Scans all blog posts for tags in format: <!-- tags: tag1, tag2 -->
Groups posts by tag, sorted alphabetically with reverse chronological posts.

Similar to generate-blog-index.py, this is a read-only script that generates
an index file without modifying source posts.
"""

import re
import glob
import os
from pathlib import Path
from collections import defaultdict


# Feature flag: Show "back to top" links after each tag section
SHOW_BACK_TO_TOP = True

# Back to top link format (used when SHOW_BACK_TO_TOP is True)
# potential up arrows: ⬆, ⬆️, 🔝, 🔼, 🔺, ↑
BACK_TO_TOP_LINK = '[↑](#tags)'

# Number of popular tags to show in the summary section
TOP_TAGS_COUNT = 7


def create_slug(tag):
    """
    Create URL-friendly slug from tag name.

    Args:
        tag: Tag name (may contain spaces)

    Returns:
        str: Slug for anchor links (spaces replaced with hyphens)
    """
    return tag.replace(' ', '-')


def extract_post_metadata(filepath):
    """
    Extract tags, title, and date from a blog post.

    Reads first 2 lines to extract:
    - Line 1: Title (# Title format)
    - Line 2: Tags (<!-- tags: tag1, tag2 --> format)

    Also extracts date from filename pattern: YYYY/YYYY-MM-DD-*

    Args:
        filepath: Path to blog post markdown file

    Returns:
        tuple: (tags_list, title, date) or ([], None, None) on error
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read only first 2 lines
            title_line = f.readline().strip()
            tags_line = f.readline().strip()

        # Extract title
        title = title_line.lstrip('#').strip()

        # Extract tags from HTML comment
        tags = []
        tag_match = re.search(r'<!--\s*tags:\s*(.+?)\s*-->', tags_line)
        if tag_match:
            tags_str = tag_match.group(1)
            tags = [tag.strip().lower() for tag in tags_str.split(',') if tag.strip()]

        # Extract date from filename: YYYY/YYYY-MM-DD-*
        date_match = re.search(r'(\d{4})/(\d{4}-\d{2}-\d{2})-', filepath)
        if date_match:
            date = date_match.group(2)
            return tags, title, date

        return tags, title, None

    except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return [], None, None


def generate_tags_page(blog_dir, output_path):
    """
    Generate docs/tags/index.md with all tags and posts.

    Scans all blog posts, extracts tags, and generates an index page with:
    - Statistics summary (post count, tag count)
    - Top 10 popular tags (clickable)
    - All tags alphabetically with their posts (reverse chronological)

    Args:
        blog_dir: Path to blog directory containing posts
        output_path: Path where tags index will be written
    """
    posts_by_tag = defaultdict(list)
    posts_without_tags = []
    unique_tagged_posts = set()  # Track unique posts with tags

    # Scan all blog posts
    pattern = os.path.join(blog_dir, '**', '*.md')
    for md_file in glob.glob(pattern, recursive=True):
        # Skip index files
        if md_file.endswith('/index.md') or md_file.endswith('\\index.md'):
            continue

        # Skip the tags index itself
        if md_file.endswith('/tags/index.md') or md_file.endswith('\\tags\\index.md'):
            continue

        # Extract metadata (single file read)
        tags, title, date = extract_post_metadata(md_file)

        if not title or not date:
            continue

        if not tags:
            posts_without_tags.append((date, title, md_file))
            continue

        # Track unique posts with tags
        unique_tagged_posts.add(md_file)

        # Relative path from tags/index.md perspective (in docs/tags/)
        rel_path = os.path.relpath(md_file, os.path.dirname(output_path))
        # Normalize path separators for consistency
        rel_path = rel_path.replace('\\', '/')

        for tag in tags:
            posts_by_tag[tag].append({
                'title': title,
                'date': date,
                'path': rel_path
            })

    # Calculate statistics
    sorted_tags = sorted(posts_by_tag.keys())
    unique_posts_count = len(unique_tagged_posts)
    unique_tags_count = len(sorted_tags)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Generate tags/index.md
    with open(output_path, 'w', encoding='utf-8') as f:
        # Write content (frontmatter handled by .meta.yml)
        f.write('# Tags\n\n')
        f.write('Browse blog posts by tag.\n\n')

        if not sorted_tags:
            f.write('*No tagged posts found.*\n')
            return

        # Get top N tags by post count
        tags_by_count = sorted(
            [(tag, len(posts_by_tag[tag])) for tag in sorted_tags],
            key=lambda x: x[1],
            reverse=True
        )
        top_tags = tags_by_count[:TOP_TAGS_COUNT]

        # Write compact statistics
        f.write(f'**📊 {unique_posts_count} posts • {unique_tags_count} tags**\n\n')

        # Write top tags inline with clickable links
        top_tags_links = []
        for tag, count in top_tags:
            slug = create_slug(tag)
            top_tags_links.append(f'[{tag} ({count})](#{slug})')
        top_tags_str = ' • '.join(top_tags_links)
        f.write(f'**Popular**: {top_tags_str}\n\n')

        # Separator
        f.write('---\n\n')

        for tag in sorted_tags:
            # Sort posts by date descending (newest first)
            posts = sorted(posts_by_tag[tag], key=lambda p: p['date'], reverse=True)
            post_count = len(posts)

            # Create heading with explicit anchor ID for clickable links
            slug = create_slug(tag)
            f.write(f'<a id="{slug}"></a>\n')

            # Add "back to top" link on heading line (if enabled)
            if SHOW_BACK_TO_TOP:
                f.write(f'## {tag} ({post_count}) {BACK_TO_TOP_LINK}\n\n')
            else:
                f.write(f'## {tag} ({post_count})\n\n')

            for post in posts:
                f.write(f'- {post["date"]} - [{post["title"]}]({post["path"]})\n')

            f.write('\n')

    # Report statistics
    print(f'✓ Generated {output_path}')
    print(f'  {unique_tags_count} tags, {unique_posts_count} tagged posts')

    if posts_without_tags:
        print(f'\nWarning: {len(posts_without_tags)} posts without tags:')
        for date, title, filepath in sorted(posts_without_tags, reverse=True):
            print(f'  - {date} - {title}')
            print(f'    {filepath}')


def main():
    """Main entry point."""
    # Paths relative to repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    blog_dir = repo_root / 'docs' / 'blog'
    output_path = repo_root / 'docs' / 'tags' / 'index.md'

    if not blog_dir.exists():
        print(f'Error: Blog directory not found: {blog_dir}')
        return 1

    print('Generating tags index...')
    generate_tags_page(str(blog_dir), str(output_path))

    return 0


if __name__ == '__main__':
    exit(main())
