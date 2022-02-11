# How to configure git diff and merge tools?
> | git | tool |

Git can use external tools to perform merge and diff:  

**Use default tool:**  

```
git difftool
git mergetool  
```
  
**Use custom tool:**

```
git difftool -t tool_name  
git mergetool -t tool_name
```

There are tons on diff/merge tools, I'd like highlight git configuration for three of them:

* [DiffMerge](http://www.sourcegear.com/diffmerge/)
* [Kdiff3](http://kdiff3.sourceforge.net/)
* [opendiff](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/opendiff.1.html)

**Sample ~/.gitconfig (Windows):**  

```
[difftool "kdiff3"]
     path = D:/Tools/KDiff3/kdiff3.exe
     keepBackup = false
     trustExitCode = false
[mergetool "kdiff3"]
     path = D:/Tools/KDiff3/kdiff3.exe
     keepBackup = false
     trustExitCode = false
[difftool "diffmerge"]
     cmd = \"C:/Program Files/SourceGear/Common/DiffMerge/sgdm.exe\"  \"$LOCAL\" \"$REMOTE\"
[mergetool "diffmerge"]
     cmd = \"D:/Tools/Git/cmd/git-diffmerge-merge.sh\" \"$BASE\" \"$LOCAL\" \"$REMOTE\" \"$MERGED\"
     trustExitCode = false

[diff]
    tool = kdiff3
[merge]
    tool = kdiff3
```

**Content of `git-diffmerge-merge.sh`:**

```bash
$cat D:/Tools/Git/cmd/git-diffmerge-merge.sh
#!/bin/sh
localPath="$2"
basePath="$1"
remotePath="$3"
resultPath="$4"
if [ ! -f $basePath ]
then
    basePath="~/diffmerge-empty"
fi
"C:/Program Files/SourceGear/Common/DiffMerge/sgdm.exe" --merge --result="$resultPath" "$localPath" "$basePath" "$remotePath" --title1="Mine" --title2="Merged: $4" --title3="Theirs"
```

**Sample `~/.gitconfig` (OS X):**

```
[diff]
    tool = opendiff
[merge]
    tool = opendiff
```

[opendiff](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/opendiff.1.html) is bundled with Xcode Tools.

Sample usage:

```
$ git difftool -t diffmerge HEAD..HEAD~1  
```

Links:  

* [How to setup KDiff as the diff tool for GIT](http://www.gitshah.com/2010/12/how-to-setup-kdiff-as-diff-tool-for-git.html) 
* [how to configure your git diff or merge tool](http://www.devinprogress.info/2012/01/how-to-configure-your-git-diff-or-merge.html) 
* [How to setup Git to use Diffmerge](http://adventuresincoding.com/2010/04/how-to-setup-git-to-use-diffmerge%20)
