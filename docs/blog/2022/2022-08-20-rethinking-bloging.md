# Rethinking Bloging
<!-- tags: blog -->

*Rethinking Bloging with simplest possible tools: Git repo, Markdown, MkDocs and GitHub Actions*

See my previous posts:

- [2018-12-31 - Thoughts about Blogging](../2018/2018-12-31-about-blogging.md)
- [2014-09-07 - Migration to Octopress](../2014/2014-09-07-migration-to-octopress.md)

## Initial thoughts

[**Mind-flow**](https://github.com/halyph/mind-flow) *repo-as-a-blog* was and is really cool idea.
I can concentrate on content only. I can write with a hope it will be useful for other people.

Unfortunately, the reality is different. I was/is lazy and didn't write enough and content is cheap.

My initial though that *repo-as-a-blog* is enough - didn't work. It's more convenient for readers to have some site.

I had several criterias for my next static site generator:

1. Git *repo-as-a-blog* is the main concept and I don’t want changing repo layout and page meta data (the status quo is *"there must be no meta data"*) to satisfy some static site generation engine (like [Hugo](https://gohugo.io) or [Jekyll](https://jekyllrb.com))
2. Rendered site must have simple design, close to Github Readme
3. Site rendering speed must be acceptable
4. I must like selected tool

## *repo-as-a-blog* concept

Static site generators come and go, but repo with content remains. I like the feeling:  
*open editor, write something and you are done. You have a new post even without static site generator.*

Site generator doesn't work, who cares. I still have my repo with my blog posts.

## Material for MkDocs

And I found [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). This tool is designed for wiki-like documentation, but not for blogging.
Nevertheless I like it a lot. It is simple and powerful at the same time. I can adjust it to my minimal needs and it just works.

The most important MkDocs feature: it does not need page related metadata, it simply renders folder's content, amazing.

When I am saying *"meta data"* I mean this:

- Hugo

```
---
layout: post
title: "My awesome blog post"
date: 2015-12-15 00:00:01
description: "An insightful description for this page that Google will like"
---
```

- JBake

```
title=Weekly Links #2
date=2013-02-01
type=post
tags=weekly links, java
status=published
~~~~~~
```

Of cause, MkDocs has meta data section, but it is not mandatory and I can skip it if I want/need.

## Github Action

I host my rendered site via Github Pages. I could deploy it manually, but it's 2022 and I can easily use Github actions for free deployment.
I've decided to use [github-action-push-to-another-repository](https://github.com/marketplace/actions/push-directory-to-another-repository). It's pretty simple and transparent, has narrow scope and well documented.

Just write post, commit and push to repo and site generation will be done automatically and transparent for me. Profit!

## Epilogue

I don't think I made any valuable contribution to the world via writing this post. It's just my *mind flow* and I like it.