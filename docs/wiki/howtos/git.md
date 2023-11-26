---
tags:
  - git
  - cut
---

# git

## Undo the Last Commit

```shell
git reset --soft HEAD~1  # you won't lose the uncommitted changes you may have
git reset --hard HEAD~1  # also remove all unstaged changes
```

## Deleting a remote branch

```shell
git push origin --delete <branch>  # Git version 1.7.0 or newer
git push origin -d <branch>        # Shorter version (Git 1.7.0 or newer)
git push origin :<branch>          # Git versions older than 1.7.0
```

## Deleting my Git branches

```shell
git branch | grep OI | grep -v OI-some-text | xargs git branch -D
```

## Batch delete remote stale branches

```shell
git branch -r | grep origin/dependabot/go_modules/ | cut -d '/' -f 2- | xargs git push origin -d
```

??? example "Sample batch delete"

    ```shell
      ➜ git branch -r | grep origin/dependabot/go_modules/ | cut -d '/' -f 2- | xargs git push origin -d
      remote:
      To github.<xyz>:name/repo.git
      - [deleted]         dependabot/go_modules/github.com/go-kit/log-0.2.0
      - [deleted]         dependabot/go_modules/github.com/go-pg/pg/v10-10.10.4
      - [deleted]         dependabot/go_modules/github.com/go-playground/locales-0.14.1
      - [deleted]         dependabot/go_modules/github.com/go-playground/validator/v10-10.11.1
      - [deleted]         dependabot/go_modules/github.com/go-testfixtures/testfixtures/v3-3.8.1
      - [deleted]         dependabot/go_modules/github.com/jarcoal/httpmock-1.2.0
      - [deleted]         dependabot/go_modules/github.com/lib/pq-1.10.7
      - [deleted]         dependabot/go_modules/github.com/stoewer/go-strcase-1.2.1
      - [deleted]         dependabot/go_modules/github.com/stretchr/testify-1.8.1
    ```

## Check out a remote Git branch

!!! note "Assumption"
    we have many remote branches

!!! info
    In earlier versions of git, you needed an explicit `--track` option, but that is the default now when you are branching off a remote branch

```shell
git fetch --all --prune
git checkout -b <branch> <remote_repo>/<remote_branch>
```
