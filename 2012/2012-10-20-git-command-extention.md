# Git command extension
> | git |

You probably know about "git config alias.*" command. See quote from documentation: 

> **alias.***
> 
> ... 
> If the alias expansion is prefixed with an exclamation point, it will be treated as a shell command. For example, defining `alias.new = !gitk --all --not ORIG_HEAD`, the invocation `git new` is equivalent to running the shell command `gitk --all --not ORIG_HEAD`. Note that shell commands will be executed from the top-level directory of a repository, which may not necessarily be the current directory.

Base on this we can define some "new" command via aliases. But, there is another way for extending git. Let's have a quick view into [git.c source](https://github.com/git/git/blob/master/git.c):

```c
int main(int argc, const char **argv)
{
    const char *cmd;

    startup_info = &git_startup_info;

    cmd = git_extract_argv0_path(argv[0]);
    if (!cmd)
    cmd = "git-help";

    git_setup_gettext();

    /*
    * "git-xxxx" is the same as "git xxxx", but we obviously:
    *
    * - cannot take flags in between the "git" and the "xxxx".
    * - cannot execute it externally (since it would just do
    * the same thing over again)
    *
    * So we just directly call the internal command handler, and
    * die if that one cannot handle it.
    */
    if (!prefixcmp(cmd, "git-")) {
        cmd += 4;
        argv[0] = cmd;
        handle_internal_command(argc, argv);
        die("cannot handle %s internally", cmd);
    }
```

It means we can define some executable peace of code (shell script, ruby script, etc.) which has prefix `git-`. Put this script on system path (add to `$PATH` variable) and it will be treated as git command.

Let's clarify all this via sample code:

```bash
$ cd ~
$ mkdir bin

$ #create git-foobar file 
$ cat > git-foobar
#!/bin/sh
echo "[foobar] commad"
^D
$ chmod +x git-foobar

$ git-foobar
[foobar] commad
$ cd ~

$ #check if ~./bin folder is in $PATH variable
$ cat .bash_profile
export PATH="$HOME/bin:$PATH"

$ #now check git 
$ git foobar
[foobar] commad
```
