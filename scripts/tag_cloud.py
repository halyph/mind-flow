#!/usr/bin/env python3
"""
Word cloud SVG generator for tags.

Uses spiral placement algorithm with collision detection to create
a visually appealing word cloud from tag data.
"""

import math


# Word cloud configuration
WORD_CLOUD_WIDTH = 800
WORD_CLOUD_HEIGHT = 600
WORD_CLOUD_MIN_FONT_SIZE = 12
WORD_CLOUD_MAX_FONT_SIZE = 48


def calculate_font_size(count, min_count, max_count, min_size=WORD_CLOUD_MIN_FONT_SIZE, max_size=WORD_CLOUD_MAX_FONT_SIZE):
    """
    Calculate font size based on post count using linear interpolation.

    Args:
        count: Post count for this tag
        min_count: Minimum post count across all tags
        max_count: Maximum post count across all tags
        min_size: Minimum font size
        max_size: Maximum font size

    Returns:
        int: Font size between min_size and max_size
    """
    if max_count == min_count:
        return max_size

    # Linear interpolation
    ratio = (count - min_count) / (max_count - min_count)
    font_size = min_size + (max_size - min_size) * ratio
    return int(font_size)


def get_tag_color(index):
    """
    Get color for tag based on its index in the popular list.

    Args:
        index: Index in the top tags list (0-based)

    Returns:
        str: Hex color code
    """
    # Color palette - cycling through a set of distinct colors
    colors = [
        '#007396',  # Java blue
        '#3776AB',  # Python blue
        '#CC342D',  # Ruby red
        '#DC322F',  # Scala red
        '#8B5CF6',  # Purple
        '#10B981',  # Green
        '#00ADD8',  # Go cyan
        '#F59E0B',  # Amber
        '#EC4899',  # Pink
        '#6366F1',  # Indigo
    ]
    return colors[index % len(colors)]


def estimate_text_bbox(tag, font_size):
    """
    Estimate bounding box for text element.

    Args:
        tag: Tag text
        font_size: Font size in pixels

    Returns:
        tuple: (width, height) of bounding box
    """
    # Rough estimation: width = 0.6 * font_size per character, height = 1.2 * font_size
    width = len(tag) * font_size * 0.6
    height = font_size * 1.2
    return width, height


def check_collision(x, y, width, height, placed_boxes, padding=5):
    """
    Check if a bounding box collides with any already placed boxes.

    Args:
        x: X coordinate (left edge)
        y: Y coordinate (top edge)
        width: Width of box
        height: Height of box
        placed_boxes: List of (x, y, width, height) tuples for placed words
        padding: Extra spacing between boxes

    Returns:
        bool: True if collision detected, False otherwise
    """
    # Add padding to the box
    x1 = x - padding
    y1 = y - padding
    x2 = x + width + padding
    y2 = y + height + padding

    for bx, by, bw, bh in placed_boxes:
        # Check if rectangles overlap
        if not (x2 < bx or x1 > bx + bw or y2 < by or y1 > by + bh):
            return True

    return False


def find_position_spiral(tag, font_size, center_x, center_y, placed_boxes, width, height):
    """
    Find position for word using spiral placement algorithm.

    Args:
        tag: Tag text
        font_size: Font size
        center_x: X coordinate of spiral center
        center_y: Y coordinate of spiral center
        placed_boxes: List of already placed bounding boxes
        width: Canvas width
        height: Canvas height

    Returns:
        tuple: (x, y) position for text baseline
    """
    text_width, text_height = estimate_text_bbox(tag, font_size)

    # Try center position first
    x = center_x - text_width / 2
    y = center_y - text_height / 2
    if not check_collision(x, y, text_width, text_height, placed_boxes):
        return x, y + text_height * 0.75  # Adjust y for text baseline

    # Spiral parameters
    angle = 0
    radius = 10
    angle_step = 0.5  # radians
    radius_step = 5
    max_radius = max(width, height)

    # Search in expanding spiral
    while radius < max_radius:
        # Calculate position on spiral
        x = center_x + radius * math.cos(angle) - text_width / 2
        y = center_y + radius * math.sin(angle) - text_height / 2

        # Check if position is valid (within bounds and no collision)
        if (0 <= x <= width - text_width and
            0 <= y <= height - text_height and
            not check_collision(x, y, text_width, text_height, placed_boxes)):
            return x, y + text_height * 0.75  # Adjust y for text baseline

        # Move along spiral
        angle += angle_step
        radius += radius_step * angle_step / (2 * math.pi)

    # No position found - fallback to center (shouldn't happen often)
    return center_x, center_y


def create_slug(tag):
    """
    Create URL-friendly slug from tag name.

    Args:
        tag: Tag name (may contain spaces)

    Returns:
        str: Slug for anchor links (spaces replaced with hyphens)
    """
    return tag.replace(' ', '-')


def calculate_content_bounds(placed_boxes, padding=40):
    """
    Calculate the bounding box of all placed content.

    Args:
        placed_boxes: List of (x, y, width, height) tuples for placed words
        padding: Extra padding around content

    Returns:
        tuple: (min_x, min_y, max_x, max_y, final_width, final_height)
    """
    if not placed_boxes:
        return 0, 0, 0, 0, 0, 0

    min_x = min(box[0] for box in placed_boxes)
    min_y = min(box[1] for box in placed_boxes)
    max_x = max(box[0] + box[2] for box in placed_boxes)
    max_y = max(box[1] + box[3] for box in placed_boxes)

    # Add padding
    min_x = max(0, min_x - padding)
    min_y = max(0, min_y - padding)
    max_x = max_x + padding
    max_y = max_y + padding

    final_width = int(max_x - min_x)
    final_height = int(max_y - min_y)

    return min_x, min_y, max_x, max_y, final_width, final_height


def generate_word_cloud_svg(tags_with_counts, output_path, width=WORD_CLOUD_WIDTH, height=WORD_CLOUD_HEIGHT, tags_limit=0, repo_root=None):
    """
    Generate word cloud SVG from tags using spiral placement.

    Creates a visual word cloud with:
    - Font sizes proportional to post counts
    - Clickable links to tag sections
    - Colors from predefined palette
    - Spiral placement algorithm with collision detection
    - Dynamic SVG sizing to minimize white space

    Args:
        tags_with_counts: List of (tag, count) tuples sorted by count descending
        output_path: Path where SVG will be written
        width: Maximum canvas width in pixels (content may be smaller)
        height: Maximum canvas height in pixels (content may be smaller)
        tags_limit: Maximum number of tags to include (0 = all)
        repo_root: Repository root path for relative path calculation (optional)
    """
    if not tags_with_counts:
        return

    # Apply limit if specified
    if tags_limit > 0:
        tags_with_counts = tags_with_counts[:tags_limit]

    # Calculate font sizes
    counts = [count for _, count in tags_with_counts]
    min_count = min(counts)
    max_count = max(counts)

    # Prepare tag data with positions using spiral placement
    tag_data = []
    placed_boxes = []
    center_x = width / 2
    center_y = height / 2

    for index, (tag, count) in enumerate(tags_with_counts):
        font_size = calculate_font_size(count, min_count, max_count)
        color = get_tag_color(index)
        slug = create_slug(tag)

        # Find position using spiral algorithm
        x, y = find_position_spiral(tag, font_size, center_x, center_y, placed_boxes, width, height)

        # Store bounding box for collision detection
        text_width, text_height = estimate_text_bbox(tag, font_size)
        placed_boxes.append((x, y - text_height * 0.75, text_width, text_height))

        tag_data.append({
            'tag': tag,
            'slug': slug,
            'font_size': font_size,
            'color': color,
            'x': x,
            'y': y,
            'bold': font_size >= 38  # Bold for larger tags
        })

    # Calculate actual content bounds
    min_x, min_y, max_x, max_y, final_width, final_height = calculate_content_bounds(placed_boxes)

    # Adjust tag positions to account for cropped space
    for td in tag_data:
        td['x'] -= min_x
        td['y'] -= min_y

    # Generate SVG with dynamic dimensions
    svg_lines = [
        f'<svg width="{final_width}" height="{final_height}" viewBox="0 0 {final_width} {final_height}"',
        '     xmlns="http://www.w3.org/2000/svg">',
        '  <style>',
        '    text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; cursor: pointer; }',
        '    text:hover { opacity: 0.7; text-decoration: underline; fill: #0969da; }',
        '  </style>',
        ''
    ]

    # Add each tag
    for td in tag_data:
        weight = 'font-weight="bold" ' if td['bold'] else ''
        svg_lines.extend([
            f'  <a href="./#{{slug}}" target="_parent">'.replace('{slug}', td['slug']),
            f'    <text x="{td["x"]}" y="{td["y"]}" font-size="{td["font_size"]}" {weight}fill="{td["color"]}">{td["tag"]}</text>',
            '  </a>',
            ''
        ])

    svg_lines.append('</svg>')

    # Write SVG file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))

    # Print with relative path if repo_root provided
    if repo_root:
        from pathlib import Path
        rel_path = Path(output_path).relative_to(repo_root)
        print(f'✓ Generated {rel_path}')
    else:
        print(f'✓ Generated {output_path}')

    # Return actual dimensions for embedding
    return final_width, final_height
