# Groovy Notes: Pretty print JSON from the command line
> | groovy |

JSON pretty print it's common task while working with JSON from command line. There are many ways of doing this via Python, Ruby, node.js, but here I'd like to concentrate on Groovy one-liner:

```bash
$ echo '{"foo": "lorem", "bar": "ipsum"}' | groovy -e 'import groovy.json.*; println JsonOutput.prettyPrint(System.in.text)'

{
    "foo": "lorem",
    "bar": "ipsum"
}
```

We can slightly improve this one-liner via adding shell alias:

```bash
$ alias pp="groovy -e 'import groovy.json.*; println JsonOutput.prettyPrint(System.in.text)'"
$ echo '{"foo": "lorem", "bar": "ipsum"}' | pp
```

Also, we might use Groovy script which might be handy for simple JSON validation also:

```groovy
$ cat prettyJson.groovy 
import groovy.json.*

try {
  println JsonOutput.prettyPrint(System.in.text)
} catch (JsonException e) {
  println "ERROR: Not valid JSON"
  System.exit(1)
}

$ echo '{"foo: "lorem", ' | groovy prettyJson.groovy
ERROR: Not valid JSON
```
