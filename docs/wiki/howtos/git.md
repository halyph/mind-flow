---
tags:
  - git
---

# git


## My base Git aliases

```
git config --global user.email "halyph@gmail.com"
git config --global user.name "Orest Ivasiv"
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.hist "log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short"
git config --global alias.cf "!cat .git/config"
```

## How to change commit author for the last commit

```
git commit --amend --author="Orest Ivasiv <halyph@gmail.com>"
```

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

## Git branch command behaves like `less`

- SO: [Git branch command behaves like 'less'](https://stackoverflow.com/questions/48341920/git-branch-command-behaves-like-less)
- [git - Release Notes v.2.16](https://github.com/git/git/blob/master/Documentation/RelNotes/2.16.0.txt#L85)

!!! info
    ```
    "git branch --list" learned to show its output through the pager by
    default when the output is going to a terminal, which is controlled
    by the pager.branch configuration variable.  This is similar to a
    recent change to "git tag --list".
    ```

```shell
git config --global pager.branch false
```
