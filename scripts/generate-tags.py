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


def extract_title_from_line(line):
    """
    Extract title from markdown heading line.

    Args:
        line: Markdown heading line (e.g., "# My Title")

    Returns:
        str: Title without markdown heading prefix
    """
    return line.lstrip('#').strip()


def extract_tags_from_line(line):
    """
    Extract tags from HTML comment line.

    Args:
        line: Line containing HTML comment (e.g., "<!-- tags: tag1, tag2 -->")

    Returns:
        list: List of lowercase tag strings, empty list if no tags found
    """
    tag_match = re.search(r'<!--\s*tags:\s*(.+?)\s*-->', line)
    if tag_match:
        tags_str = tag_match.group(1)
        return [tag.strip().lower() for tag in tags_str.split(',') if tag.strip()]
    return []


def extract_date_from_filepath(filepath):
    """
    Extract date from filepath pattern YYYY/YYYY-MM-DD-*.

    Args:
        filepath: Path to blog post (e.g., "docs/blog/2024/2024-01-15-title.md")

    Returns:
        str: Date in YYYY-MM-DD format, or None if not found
    """
    date_match = re.search(r'(\d{4})/(\d{4}-\d{2}-\d{2})-', filepath)
    if date_match:
        return date_match.group(2)
    return None


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
            title_line = f.readline().strip()
            tags_line = f.readline().strip()

        title = extract_title_from_line(title_line)
        tags = extract_tags_from_line(tags_line)
        date = extract_date_from_filepath(filepath)

        return tags, title, date

    except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return [], None, None


def should_skip_file(filepath):
    """
    Check if file should be skipped during tag scanning.

    Args:
        filepath: Path to markdown file

    Returns:
        bool: True if file should be skipped, False otherwise
    """
    # Skip index files
    if filepath.endswith('/index.md') or filepath.endswith('\\index.md'):
        return True

    # Skip the tags index itself
    if filepath.endswith('/tags/index.md') or filepath.endswith('\\tags\\index.md'):
        return True

    return False


def calculate_tag_statistics(posts_by_tag, unique_tagged_posts):
    """
    Calculate statistics from collected tag data.

    Args:
        posts_by_tag: Dictionary mapping tags to post lists
        unique_tagged_posts: Set of unique post filepaths with tags

    Returns:
        tuple: (sorted_tags, unique_posts_count, unique_tags_count)
    """
    sorted_tags = sorted(posts_by_tag.keys())
    unique_posts_count = len(unique_tagged_posts)
    unique_tags_count = len(sorted_tags)
    return sorted_tags, unique_posts_count, unique_tags_count


def calculate_top_tags(posts_by_tag, sorted_tags, limit=TOP_TAGS_COUNT):
    """
    Calculate top tags by post count.

    Args:
        posts_by_tag: Dictionary mapping tags to post lists
        sorted_tags: List of all tags (sorted alphabetically)
        limit: Maximum number of top tags to return

    Returns:
        list: List of (tag, count) tuples sorted by count descending
    """
    tags_by_count = sorted(
        [(tag, len(posts_by_tag[tag])) for tag in sorted_tags],
        key=lambda x: x[1],
        reverse=True
    )
    return tags_by_count[:limit]


def format_popular_tags_line(top_tags):
    """
    Format popular tags as inline links.

    Args:
        top_tags: List of (tag, count) tuples

    Returns:
        str: Formatted string like "[python (42)](#python) • [golang (35)](#golang)"
    """
    top_tags_links = []
    for tag, count in top_tags:
        slug = create_slug(tag)
        top_tags_links.append(f'[{tag} ({count})](#{slug})')
    return ' • '.join(top_tags_links)


def write_tags_page_header(f, sorted_tags, unique_posts_count, unique_tags_count, posts_by_tag):
    """
    Write header section of tags page.

    Args:
        f: File handle to write to
        sorted_tags: List of all tags (sorted alphabetically)
        unique_posts_count: Number of unique posts with tags
        unique_tags_count: Number of unique tags
        posts_by_tag: Dictionary mapping tags to post lists
    """
    # Write content (frontmatter handled by .meta.yml)
    f.write('# Tags\n\n')
    f.write('Browse blog posts by tag.\n\n')

    if not sorted_tags:
        f.write('*No tagged posts found.*\n')
        return

    # Get top N tags by post count
    top_tags = calculate_top_tags(posts_by_tag, sorted_tags)

    # Write compact statistics
    f.write(f'**📊 {unique_posts_count} posts • {unique_tags_count} tags**\n\n')

    # Write top tags inline with clickable links
    top_tags_str = format_popular_tags_line(top_tags)
    f.write(f'**Popular**: {top_tags_str}\n\n')

    # Separator
    f.write('---\n\n')


def write_tag_section(f, tag, posts):
    """
    Write a single tag section with its posts.

    Args:
        f: File handle to write to
        tag: Tag name
        posts: List of posts (already sorted by date descending)
    """
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


def collect_posts_by_tag(blog_dir, output_path):
    """
    Scan blog posts and collect tag data.

    Args:
        blog_dir: Path to blog directory containing posts
        output_path: Path where tags index will be written (used for relative paths)

    Returns:
        tuple: (posts_by_tag, posts_without_tags, unique_tagged_posts)
            - posts_by_tag: dict mapping tags to post lists
            - posts_without_tags: list of (date, title, filepath) tuples
            - unique_tagged_posts: set of unique post filepaths with tags
    """
    posts_by_tag = defaultdict(list)
    posts_without_tags = []
    unique_tagged_posts = set()

    # Scan all blog posts
    pattern = os.path.join(blog_dir, '**', '*.md')
    for md_file in glob.glob(pattern, recursive=True):
        # Skip index files and tags index
        if should_skip_file(md_file):
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

    return posts_by_tag, posts_without_tags, unique_tagged_posts


def report_generation_results(output_path, unique_tags_count, unique_posts_count, posts_without_tags):
    """
    Report generation results to console.

    Args:
        output_path: Path where tags index was written
        unique_tags_count: Number of unique tags
        unique_posts_count: Number of unique posts with tags
        posts_without_tags: List of (date, title, filepath) tuples for posts without tags
    """
    # Report statistics
    print(f'✓ Generated {output_path}')
    print(f'  {unique_tags_count} tags, {unique_posts_count} tagged posts')

    if posts_without_tags:
        print(f'\nWarning: {len(posts_without_tags)} posts without tags:')
        for date, title, filepath in sorted(posts_without_tags, reverse=True):
            print(f'  - {date} - {title}')
            print(f'    {filepath}')


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
    # Phase 1: Data Collection
    posts_by_tag, posts_without_tags, unique_tagged_posts = collect_posts_by_tag(
        blog_dir, output_path
    )

    # Phase 2: Statistics Calculation
    sorted_tags, unique_posts_count, unique_tags_count = calculate_tag_statistics(
        posts_by_tag, unique_tagged_posts
    )

    # Phase 3: File Setup
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Phase 4: Write Content
    with open(output_path, 'w', encoding='utf-8') as f:
        write_tags_page_header(
            f, sorted_tags, unique_posts_count, unique_tags_count, posts_by_tag
        )

        # Early return if no tags (handled in header)
        if not sorted_tags:
            return

        for tag in sorted_tags:
            posts = sorted(posts_by_tag[tag], key=lambda p: p['date'], reverse=True)
            write_tag_section(f, tag, posts)

    # Phase 5: Console Reporting
    report_generation_results(
        output_path, unique_tags_count, unique_posts_count, posts_without_tags
    )


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
