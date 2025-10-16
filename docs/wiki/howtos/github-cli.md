---
tags:
  - github
---

# GitHub CLI

## Reference

- [GitHub CLI manual](https://cli.github.com/manual/)

## Managing Multiple GitHub Accounts

  Now you have both accounts available:
  - Personal: `halyph` (active) - for personal repositories
  - Enterprise: `orest-corp` - for enterprise repositories

  You can switch between them using:

```shell
➜ gh auth switch --user halyph     # Switch to personal account
➜ gh auth switch --user orest-corp # Switch to enterprise account
```

## Display active account

```shell
➜ gh auth status
```

??? example

    ```bash
    ➜ gh auth status
    github.com
    ✓ Logged in to github.com account halyph (keyring)
    - Active account: true
    - Git operations protocol: ssh
    - Token: gho_************************************
    - Token scopes: 'gist', 'read:org', 'repo'

    ✓ Logged in to github.com account orest-corp (keyring)
    - Active account: false
    - Git operations protocol: ssh
    - Token: gho_************************************
    - Token scopes: 'gist', 'read:org', 'repo'
    ```