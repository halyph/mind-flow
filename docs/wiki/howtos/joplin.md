---
tags:
  - joplin
---

# Joplin

## Set TOC depth to 2nd level

- [Desktop, Mobile: Update Markdown plugins: toc-done-right, anchor #2005](https://github.com/laurent22/joplin/pull/2005)

### Default TOC

Generate table of contents automatically:

```text
[TOC]
```

??? example

    ![Alt text](joplin/toc-std.png)

### Custom TOC levels

render only 2nd level:

```text
$<toc{"level":[2]}>
```

render levels 2,3 and 4:

```text
$<toc{"level":[2,3,4],"listType":"ol"}>
```

??? example

    ![Alt text](joplin/toc-2-3-4.png)

## Hide horizontal lines in the markdown pane

- [Horizontal Lines being rendered in the markdown pane on Solarized Themes #4210](https://github.com/laurent22/joplin/issues/4210)

> This is a feature of the Solarized theme that Joplin relies on. If you don't like the line you can switch to another theme, or use custom css to style Joplin however you like.

I switched to default Dark theme and it works properly

- Solarized theme
![Alt text](joplin/hline_solar.png)

- Dark theme
![Alt text](joplin/hline_dark.png)
