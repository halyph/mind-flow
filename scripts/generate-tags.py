#!/usr/bin/env python3
"""
Generate docs/tags.md from HTML comment tags in blog posts.

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


def extract_tags_from_comment(filepath):
    """
    Extract tags from HTML comment on line 2.

    Expected format: <!-- tags: tag1, tag2, multi word tag -->

    Returns:
        list: List of tags (lowercase, stripped), or empty list if no tags found
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                # Match: <!-- tags: tag1, tag2, multi word tag -->
                match = re.search(r'<!--\s*tags:\s*(.+?)\s*-->', lines[1])
                if match:
                    tags_str = match.group(1)
                    # Split by comma, strip whitespace, lowercase
                    tags = [tag.strip().lower() for tag in tags_str.split(',') if tag.strip()]
                    return tags
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")

    return []


def extract_title_and_date(filepath):
    """
    Extract title from line 1 and date from filename.

    Title format: # Title on first line
    Date format: YYYY/YYYY-MM-DD-* in filename

    Returns:
        tuple: (title, date) or (title, None) if date not found
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            title_line = f.readline().strip()
            title = title_line.lstrip('#').strip()

        # Extract date from filename: YYYY/YYYY-MM-DD-*
        match = re.search(r'(\d{4})/(\d{4}-\d{2}-\d{2})-', filepath)
        if match:
            date = match.group(2)
            return title, date

        return title, None
    except Exception as e:
        print(f"Warning: Could not extract title/date from {filepath}: {e}")
        return None, None


def generate_tags_page(blog_dir, output_path):
    """
    Generate docs/blog/tags.md with all tags and posts.

    Format:
    # Tags

    ## tag-name
    - YYYY-MM-DD - [Post Title](path/to/post.md)
    - YYYY-MM-DD - [Another Post](path/to/post.md)

    ## another-tag
    ...
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

        # Skip the tags.md itself
        if md_file.endswith('/tags.md') or md_file.endswith('\\tags.md'):
            continue

        tags = extract_tags_from_comment(md_file)
        title, date = extract_title_and_date(md_file)

        if not title or not date:
            continue

        if not tags:
            posts_without_tags.append((date, title, md_file))
            continue

        # Track unique posts with tags
        unique_tagged_posts.add(md_file)

        # Relative path from tags.md perspective (in docs/blog/)
        rel_path = os.path.relpath(md_file, os.path.dirname(output_path))
        # Normalize path separators for consistency
        rel_path = rel_path.replace('\\', '/')

        for tag in tags:
            posts_by_tag[tag].append({
                'title': title,
                'date': date,
                'path': rel_path
            })

    # Generate tags.md
    with open(output_path, 'w', encoding='utf-8') as f:
        # Write frontmatter
        f.write('---\n')
        f.write('hide:\n')
        f.write('  - navigation\n')
        f.write('---\n\n')

        # Write content
        f.write('# Tags\n\n')
        f.write('Browse blog posts by tag.\n\n')

        # Sort tags alphabetically
        sorted_tags = sorted(posts_by_tag.keys())

        if not sorted_tags:
            f.write('*No tagged posts found.*\n')
            return

        for tag in sorted_tags:
            # Create heading with tag name
            f.write(f'## {tag}\n\n')

            # Sort posts by date descending (newest first)
            posts = sorted(posts_by_tag[tag], key=lambda p: p['date'], reverse=True)

            for post in posts:
                f.write(f'- {post["date"]} - [{post["title"]}]({post["path"]})\n')

            f.write('\n')

    # Report statistics
    unique_posts_count = len(unique_tagged_posts)
    unique_tags_count = len(sorted_tags)

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
    output_path = repo_root / 'docs' / 'tags.md'

    if not blog_dir.exists():
        print(f'Error: Blog directory not found: {blog_dir}')
        return 1

    print('Generating tags index...')
    generate_tags_page(str(blog_dir), str(output_path))

    return 0


if __name__ == '__main__':
    exit(main())
