---
tags:
  - mkdocs
---

# Mkdocs Material

## Official doc

- [Search the icon and emoji](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)
- [Repository icon](https://squidfunk.github.io/mkdocs-material/setup/adding-a-git-repository/#repository-icon)

## Plugins

:star: [mkdocs/catalog](https://github.com/mkdocs/catalog) is a list of awesome MkDocs projects and plugins.

### Selected

- [**mkdocs-awesome-pages-plugin**](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) sorts pages in navigation section (descending order)
- [**mkdocs-git-revision-date-localized-plugin**](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin) adds the date on which a Markdown file was last updated at the bottom of each page
- [**mkdocs-rss-plugin**](https://github.com/Guts/mkdocs-rss-plugin) generates a RSS feeds for created and updated pages, using git log and YAML frontmatter (page.meta)
- [**mkdocs-section-index**](https://oprypin.github.io/mkdocs-section-index/) allows clickable sections that lead to an index page.
- [**mkdocs-literate-nav**](https://oprypin.github.io/mkdocs-literate-nav/) specifies the navigation in Markdown instead of YAML
- [**mkdocs-gen-files**](https://oprypin.github.io/mkdocs-gen-files/) programmatically generate documentation pages during the build
- [**mkdocs-same-dir**](https://oprypin.github.io/mkdocs-same-dir/) allows placing `mkdocs.yml`` in the same directory as documentation
- [**mkdocstrings**](https://github.com/mkdocstrings/mkdocstrings) automatic documentation from sources

## Deployment

- [github-action-push-to-another-repository](https://github.com/marketplace/actions/push-directory-to-another-repository)
- [mkdocs-material *Github Action*](https://github.com/squidfunk/mkdocs-material/blob/master/.github/workflows/documentation.yml) - clean sample for site deployment

## Tips and Tricks

### Code blocks

I have discovered that enabling code block title and line numbers globally (in `mkdocs.yml`) is bad idea: 

```yaml title="mkdocs.yml"
markdown_extensions:
- pymdownx.highlight: # (1)!
    auto_title: true
    linenums: true
```

1. Code annotations [PyMdown Extensions - Highlight options](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/#options)


that's why I will switch on title and line numbers on demand (see more [here](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)):

```` markdown title="Code block with title"
``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
````

<div class="result" markdown>

``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

</div>

```` markdown title="Code block with line numbers"
``` py linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
````

<div class="result" markdown>

``` py linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

</div>