# [WIP] Verify Ruby `github/markup` gem for markdown rendering
<!-- tags: ruby, markdown, github -->

I've cloned [github/markup](https://github.com/github/markup) and tried to built my own Docker image:

```
docker build -t halyph/markup .
```

But there was some error

```
Step 22/26 : COPY Gemfile.lock .
COPY failed: stat /var/lib/docker/tmp/docker-builder774079505/Gemfile.lock: no such file or directory
```

The easiest solution for solving this problem is commenting the next line `# COPY Gemfile.lock .` And run `docker build` again.
Also, do not forget to push the newly created image to Docker Hub:

```
docker push halyph/markup
```

Now, I can try to run `github/markup` on some local/test files.

Lol, I noticed that this Docker file does not support my needs :-/ I need to fix it a bit.

## References

- [github/markup](https://github.com/github/markup)
- How to run `github/markup` Docker image: https://github.com/yokogawa-k/docker-github-markup.
