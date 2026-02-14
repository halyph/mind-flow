#!/usr/bin/env python3
"""
Validate that all blog posts have tags in HTML comment format.

Checks that:
- All blog posts have line 2 with <!-- tags: ... --> format
- Tags are not empty

Used for CI validation and pre-commit checks.
"""

import re
import glob
import os
from pathlib import Path


def validate_post_tags(filepath):
    """
    Check if post has valid tags comment on line 2.

    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return False, f'Could not read file: {e}'

    if len(lines) < 2:
        return False, 'File has less than 2 lines'

    tag_line = lines[1].strip()

    # Check for HTML comment format
    match = re.search(r'<!--\s*tags:\s*(.+?)\s*-->', tag_line)

    if not match:
        return False, 'Missing or invalid tags comment on line 2'

    # Extract tags
    tags_str = match.group(1)
    tags = [t.strip() for t in tags_str.split(',') if t.strip()]

    if not tags:
        return False, 'Tags comment exists but no tags found'

    return True, None


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    blog_dir = repo_root / 'docs' / 'blog'

    if not blog_dir.exists():
        print(f'Error: Blog directory not found: {blog_dir}')
        return 1

    print('Validating blog post tags...\n')

    issues = []
    valid_count = 0
    pattern = os.path.join(blog_dir, '**', '*.md')

    for md_file in glob.glob(pattern, recursive=True):
        # Skip index files
        if md_file.endswith('/index.md') or md_file.endswith('\\index.md'):
            continue

        # Skip tags.md
        if md_file.endswith('/tags.md') or md_file.endswith('\\tags.md'):
            continue

        is_valid, error_msg = validate_post_tags(md_file)

        if not is_valid:
            # Make path relative for cleaner output
            rel_path = os.path.relpath(md_file, repo_root)
            issues.append((rel_path, error_msg))
        else:
            valid_count += 1

    # Report results
    print(f'{"="*60}')
    if issues:
        print(f'✗ Validation failed: {len(issues)} issue(s) found\n')
        for filepath, error in issues:
            print(f'  {filepath}')
            print(f'    → {error}\n')
        print(f'{"="*60}')
        print(f'Valid posts: {valid_count}')
        print(f'Invalid posts: {len(issues)}')
        print('\nTo fix:')
        print('- Add tags on line 2: <!-- tags: tag1, tag2 -->')
        print('- Ensure tags are lowercase and comma-separated')
        return 1
    else:
        print(f'✓ All blog posts have valid tags')
        print(f'{"="*60}')
        print(f'Validated: {valid_count} posts')
        return 0


if __name__ == '__main__':
    exit(main())
