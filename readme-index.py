#!/usr/bin/env python3

import glob
from collections import defaultdict

README_HEADER = """# Mind~Flow

[`linkedin`](https://www.linkedin.com/in/oivasiv/) · [`bookshelf`](docs/bookshelf.md)

_Another attempt of blogging or personal knowledge base_

![logo.png](docs/assets/images/logo.png)
"""

MKDOCS_HEADER = """---
hide:
  - navigation
---

# Blog Posts

<div class="note inline end"> <p><img alt="assets/logo.png" src="../assets/images/logo.png"></p> </div>
"""

#-----------------------------------------------------------------------------------------

# Simple ugly script to generate README.md

year_format = 'YYYY'
date_format = 'YYYY-MM-DD'
README_INDEX_FILE = 'README.md'
MKDOCS_INDEX_FILE = 'docs/blog/index.md'
PREFIX = 'docs/blog/'

def define_date_ranges():
    start = len(PREFIX) + len(year_format) + len('/')
    end = start + len(date_format)
    return (start, end)

date_start, date_end = define_date_ranges()

def read_line(file_name):
    with open(file_name) as f:
        first_line = f.readline()
        return first_line

def list_files():
    files = glob.glob(PREFIX + '**/*.md', recursive=True)
    pair = [f for f in files if '/' in f and not f.startswith('misc') and not f.endswith('index.md') ] 
    return pair

def extract_date(line):
    date =  line[date_start:date_end]
    year = date[:len(year_format)]
    return (date, year)

def write_index_to_file(file, keep_prefix = True):
    post_by_year = defaultdict(list)

    for file_name in list_files():
        title = read_line(file_name)[1:-1].strip() # remove leading `# ` and strip spaces
        date, year = extract_date(file_name)
        file_name_write = file_name if keep_prefix else file_name[len(PREFIX):]
        line = f"{date} - [{title}]({file_name_write})"
        post_by_year[year].append(line)

    for year in sorted(post_by_year.keys(), reverse = True):
        print(f"\n## {year}\n", file=file)
        for year_line in sorted(post_by_year[year], reverse = True):
            print(f"- {year_line}", file=file)

def main():
    with open(README_INDEX_FILE, 'w') as f:
        f.write(README_HEADER)
        write_index_to_file(f)

    with open(MKDOCS_INDEX_FILE, 'w') as f:
        f.write(MKDOCS_HEADER)
        write_index_to_file(f, keep_prefix=False)

if __name__ == "__main__":
    main()