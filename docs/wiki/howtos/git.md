---
tags:
  - git
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