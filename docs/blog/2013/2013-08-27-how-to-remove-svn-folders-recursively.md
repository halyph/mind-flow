# How to remove .svn folders recursively?
> | bash |

Validate the list of folders which will be removed:

```bash
$ find . -name .svn -exec ls {} \;
```

Run recursive remove:

```bash
$ find . -name .svn -exec rm -rf {} \;
```

This script is run from the current folder.  Be sure you've specified `find -name` properly.

## References

- [How to remove all .svn directories from my application directories ](https://stackoverflow.com/questions/1294590/how-to-remove-all-svn-directories-from-my-application-directories)