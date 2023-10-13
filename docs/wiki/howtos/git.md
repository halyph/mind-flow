---
tags:
  - git
---

[git-reset]: https://www.freecodecamp.org/news/git-revert-commit-how-to-undo-the-last-commit/ "Git Revert Commit – How to Undo the Last Commit"

# git

## Undo the Last Commit

[Source][git-reset]

### soft reset

??? note

    The `--soft` option means that you will not lose the uncommitted changes you may have.

```shell
git reset --soft HEAD~1
```

### hard reset

??? note
  
    If you want to reset to the last commit and also remove all unstaged changes, you can use the `--hard` option

```shell
git reset --hard HEAD~1
```

## Deleting a remote branch

```shell
git push origin --delete <branch>  # Git version 1.7.0 or newer
git push origin -d <branch>        # Shorter version (Git 1.7.0 or newer)
git push origin :<branch>          # Git versions older than 1.7.0
```