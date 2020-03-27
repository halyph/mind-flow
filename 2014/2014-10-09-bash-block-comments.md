# How to use block comments in Bash Script
> | bash |

What is the simplest way to define block comment in Bash script?

I've selected two approaches for myself:

- Use here document

``` bash
#!/usr/bin/env bash

echo "before block comment"
: <<'END'
Some long 
myltiline 
text
END
echo "after block comment"
```

- Use **"if"** false block

``` bash
#!/usr/bin/env bash

echo "before block comment"
if [ ]; then 
Some long 
myltiline 
text
fi
echo "after block comment"
```
