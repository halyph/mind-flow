#!/usr/bin/env python3

import os
import glob
from collections import defaultdict

README_HEADER = """# Mind~Flow

[[twitter](https://twitter.com/halyph)]  [[linkedin](https://www.linkedin.com/in/oivasiv/)]

_Another try of blogging or personal knowledge base_

![logo.png](logo.png)
"""
#-----------------------------------------------------------------------------------------

# Simple ugly script to generate README.md

year_format = 'YYYY'
date_format = 'YYYY-MM-DD'
INDEX_FILE = 'README.md'

def read_line(file_name):
    with open(file_name) as f:
        first_line = f.readline()
        return first_line

def list_files():
    files = glob.glob('**/*.md', recursive=True)
    pair = [f for f in files if '/' in f] 
    return pair

def define_date_ranges():
    start = len(year_format) + len('/')
    end = start + len(date_format)
    return (start, end)

(date_start, date_end) = define_date_ranges()

def extract_date(line):
    date =  line[date_start:date_end]
    year = date[:len(year_format)]
    return (date, year)

post_by_year = defaultdict(list)

def write_index_to_file(file):
    for file_name in list_files():
        title = read_line(file_name)[1:-1].strip() # remove leading `# ` and strip spaces
        (date, year) = extract_date(file_name)
        line = f"{date} - [{title}]({file_name})"
        post_by_year[year].append(line)

    for year in sorted(post_by_year.keys(), reverse = True):
        print(f"\n## {year}\n", file=file)
        for year_line in sorted(post_by_year[year], reverse = True):
            print(f"- {year_line}", file=file)



with open(INDEX_FILE, 'w') as f:
    f.write(README_HEADER)
    write_index_to_file(f)