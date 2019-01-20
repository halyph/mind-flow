# Python vs Javascript comparison
> **tags**: [python] [javascript] [vs]

First of all it's not my writings and it's just a copy of posts from [@DjangoTricks](https://djangotricks.blogspot.com) blog by Aidas Bendoraitis (see [References](#references) below)

- [References](#references)
- [Parsing integers](#parsing-integers)
- [Conditional assignment](#conditional-assignment)
- [Object attribute value by attribute name](#object-attribute-value-by-attribute-name)
- [Dictionary value by key](#dictionary-value-by-key)
- [Slicing lists and strings](#slicing-lists-and-strings)
- [Operations with list items](#operations-with-list-items)
- [Joining lists of strings](#joining-lists-of-strings)
- [JSON](#json)
- [Working with Strings](#working-with-strings)
  - [Splitting strings by regular expressions](#splitting-strings-by-regular-expressions)
  - [Matching regular expression patterns in strings](#matching-regular-expression-patterns-in-strings)
  - [Search sub-string](#search-sub-string)
  - [Replacing patterns in strings using regular expressions](#replacing-patterns-in-strings-using-regular-expressions)
  - [Replacing patterns in strings using a function call](#replacing-patterns-in-strings-using-a-function-call)
- [Error handling](#error-handling)
- [Variables in strings](#variables-in-strings)
- [Unpacking lists](#unpacking-lists)
- [Lambda functions](#lambda-functions)
- [Iteration without indexes](#iteration-without-indexes)
- [Generators](#generators)
- [Sets](#sets)
- [Function arguments](#function-arguments)
- [Classes and inheritance](#classes-and-inheritance)
- [Class properties: getters and setters](#class-properties-getters-and-setters)

## References

- [Equivalents in Python and JavaScript. Part 1](https://djangotricks.blogspot.com/2018/06/equivalents-in-python-and-javascript-part-1.html)
- [Equivalents in Python and JavaScript. Part 2](https://djangotricks.blogspot.com/2018/07/equivalents-in-python-and-javascript-part-2.html)
- [Equivalents in Python and JavaScript. Part 3](https://djangotricks.blogspot.com/2018/07/equivalents-in-python-and-javascript-part-3.html)
- [Equivalents in Python and JavaScript. Part 4](https://djangotricks.blogspot.com/2018/07/equivalents-in-python-and-javascript-part-4.html)

---

## Parsing integers

**Python**

```python
number = int(text)
```

**JavaScript**

```javascript
number = parseInt(text, 10);

parseInt('012') == 10;  // in some older browsers
parseInt('012', 10) == 12;
```

## Conditional assignment

**Python**

```python
value = 'ADULT' if age >= 18 else 'CHILD'
```

**JavaScript**

```javascript
value = age >= 18? 'ADULT': 'CHILD';
```

## Object attribute value by attribute name

**Python** and **JavaScript**

```
obj.color = 'YELLOW'
```

**Python**

```python
attribute = 'color'
value = getattr(obj, attribute, 'GREEN')
setattr(obj, attribute, value)
```

**JavaScript**

```javascript
attribute = 'color';
value = obj[attribute] || 'GREEN';
obj[attribute] = value;
```

## Dictionary value by key

**Python** and **JavaScript**

```
dictionary = {}
dictionary['color'] = 'YELLOW'
```

**Python**

```python
key = 'color'
val1 = dictionary[key]
val2 = dictionary.get('non-existing keys') # The more flexible way is to use the get() method which returns None for non-existing keys.
value = dictionary.get(key, 'GREEN') # you can pass an optional default value as the second parameter
```

**JavaScript**

```javascript
key = 'color';
value = dictionary[key] || 'GREEN';
```

## Slicing lists and strings

**Python**

```python
items = [1, 2, 3, 4, 5]
first_two = items[:2]      # [1, 2]
last_two = items[-2:]      # [4, 5]
middle_three = items[1:4]  # [2, 3, 4]

# The [:] slice operator in Python also works for strings:
text = 'ABCDE'
first_two = text[:2]      # 'AB'
last_two = text[-2:]      # 'DE'
middle_three = text[1:4]  # 'BCD'
```

**JavaScript**

```javascript
items = [1, 2, 3, 4, 5];
first_two = items.slice(0, 2);     // [1, 2]
last_two = items.slice(-2);        // [4, 5]
middle_three = items.slice(1, 4);  // [2, 3, 4]

// In JavaScript strings just like arrays have the slice() method:
text = 'ABCDE';
first_two = text.slice(0, 2);    // 'AB'
last_two = text.slice(-2);       // 'DE'
middle_three = text.slice(1, 4); // 'BCD'
```

## Operations with list items

**Python**

```python
items1 = ['A']
items2 = ['B']
items = items1 + items2  # items == ['A', 'B']
items.append('C')        # ['A', 'B', 'C']
items.insert(0, 'D')     # ['D', 'A', 'B', 'C']
first = items.pop(0)     # ['A', 'B', 'C']
last = items.pop()       # ['A', 'B']
items.delete(0)          # ['B']
```

**JavaScript**

```javascript
items1 = ['A'];
items2 = ['B'];
items = items1.concat(items2);  // items === ['A', 'B']
items.push('C');                // ['A', 'B', 'C']
items.unshift('D');             // ['D', 'A', 'B', 'C']
first = items.shift();          // ['A', 'B', 'C']
last = items.pop();             // ['A', 'B']
items.splice(0, 1);             // ['B']
```

## Joining lists of strings

**Python**

```python
items = ['A', 'B', 'C']
text = ', '.join(items)  # 'A, B, C'
```

**JavaScript**

```javascript
items = ['A', 'B', 'C'];
text = items.join(', ');  // 'A, B, C'
```

## JSON

**Python**

```python
import json
json_data = json.dumps(dictionary, indent=4)
dictionary = json.loads(json_data)
```

**JavaScript**

```javascript
json_data = JSON.stringify(dictionary, null, 4);
dictionary = JSON.parse(json_data);
```

## Working with Strings

### Splitting strings by regular expressions

**Python**

```python
import re

# One or more characters of "!?." followed by whitespace
delimiter = re.compile(r'[!?\.]+\s*')

text = "Hello!!! What's new? Follow me."
sentences = delimiter.split(text)
# sentences == ['Hello', "What's new", 'Follow me', '']
```

**JavaScript**

```javascript
// One or more characters of "!?." followed by whitespace
delimiter = /[!?\.]+\s*/;

text = "Hello!!! What's new? Follow me.";
sentences = text.split(delimiter)
// sentences === ["Hello", "What's new", "Follow me", ""]
```

### Matching regular expression patterns in strings

**Python**

```python
import re

# name, "@", and domain
pattern = re.compile(r'([\w.+\-]+)@([\w\-]+\.[\w\-.]+)')

match = pattern.match('hi@example.com')
# match.group(0) == 'hi@example.com'
# match.group(1) == 'hi'
# match.group(2) == 'example.com'
```

**JavaScript**

```javascript
// name, "@", and domain
pattern = /([\w.+\-]+)@([\w\-]+\.[\w\-.]+)/;

match = 'hi@example.com'.match(pattern);
// match[0] === 'hi@example.com'
// match[1] === 'hi'
// match[2] === 'example.com'
```

### Search sub-string

**Python**

```python
text = 'Say hi at hi@example.com'
first_match = pattern.search(text)
if first_match:
    start = first_match.start()  # start == 10
```

**JavaScript**

```javascript
text = 'Say hi at hi@example.com';
first_match = text.search(pattern);
if (first_match > -1) {
    start = first_match;  // start === 10
}
```

### Replacing patterns in strings using regular expressions

**Python**

```python
# In Python the captures, also called as "backreferences", are accessible in the replacement string as \g<0>, \g<1>, \g<2>

html = pattern.sub(
    r'<a href="mailto:\g<0>">\g<0></a>',
    'Say hi at hi@example.com',
)
# html == 'Say hi at <a href="mailto:hi@example.com">hi@example.com</a>'
```

**JavaScript**

```javascript
// In JavaScript the same is accessible as $&, $1, $2, etc.

html = 'Say hi at hi@example.com'.replace(
    pattern, 
    '<a href="mailto:$&">$&</a>',
);
// html === 'Say hi at <a href="mailto:hi@example.com">hi@example.com</a>'
```

### Replacing patterns in strings using a function call

**Python**

```python
text = pattern.sub(
    lambda match: match.group(0).upper(), 
    'Say hi at hi@example.com',
)
# text == 'Say hi at HI@EXAMPLE.COM'
```

**JavaScript**

```javascript
text = 'Say hi at hi@example.com'.replace(
    pattern,
    function(match, p1, p2) {
        return match.toUpperCase();
    }
);
// text === 'Say hi at HI@EXAMPLE.COM'
```

## Error handling

**Python**

```python
class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def proceed():
    raise MyException('Error happened!')

try:
    proceed()
except MyException as err:
    print('Sorry! {}'.format(err))
finally:
    print('Finishing')
```

**JavaScript**

```javascript
function MyException(message) {
   this.message = message;
   this.toString = function() {
       return this.message;
   }
}

function proceed() {
    throw new MyException('Error happened!');
}

try {
    proceed();
} catch (err) {
    if (err instanceof MyException) {
        console.log('Sorry! ' + err);
    }
} finally {
    console.log('Finishing');
}
```

## Variables in strings

```
name = 'World'
value = 'Hello, ' + name + '!\nWelcome!'
```

**Python**

```python
name = 'World'
value = f"""Hello, {name}!
Welcome!"""

price = 14.9
value = f'Price: {price:.2f} €'  # 'Price: 14.90 €'
```

**JavaScript**

```javascript
name = 'World';
value = `Hello, ${name}!
Welcome!`;

price = 14.9;
value = `Price ${price.toFixed(2)} €`;  // 'Price: 14.90 €'
```

## Unpacking lists

**Python**

```python
[a, b, c] = [1, 2, 3]

# E.g. popular variable swap
a = 1
b = 2
a, b = b, a  # swap values

# Python 3.6
first, second, *the_rest = [1, 2, 3, 4]
# first == 1
# second == 2
# the_rest == [3, 4]
```

**JavaScript**

```javascript
// ECMAScript 6
[first, second, ...the_rest] = [1, 2, 3, 4];
// first === 1
// last === 2
// the_rest === [3, 4]
```

## Lambda functions

**Python**

```python
sum = lambda x, y: x + y
square = lambda x: x ** 2
```

**JavaScript**

```javascript
sum = (x, y) => x + y;
square = x => Math.pow(x, 2);
```

## Iteration without indexes

**Python**

```python
for item in ['A', 'B', 'C']:
    print(item)

for character in 'ABC':
    print(character)
```

**JavaScript**

```javascript
for (let item of ['A', 'B', 'C']) {
    console.log(item);
}

for (let character of 'ABC') {
    console.log(character);
}
```

## Generators

**Python**

```python
def countdown(counter):
    while counter > 0:
        yield counter
        counter -= 1

for counter in countdown(10):
    print(counter)
```

**JavaScript**

```javascript
function* countdown(counter) {
    while (counter > 0) {
        yield counter;
        counter--;
    }
}
for (let counter of countdown(10)) {
    console.log(counter);
}
```

## Sets

**Python**

```python
s = set(['A'])
s.add('B'); s.add('C')
'A' in s
len(s) == 3
for elem in s:
    print(elem)
s.remove('C')
```

**JavaScript**

```javascript
s = new Set(['A']);
s.add('B').add('C');
s.has('A') === true;
s.size === 3;
for (let elem of s.values()) {
    console.log(elem);
}
s.delete('C')
```

## Function arguments

**Python**

```python
from pprint import pprint

def report(post_id, reason='not-relevant'):
    pprint({'post_id': post_id, 'reason': reason})

report(42)
report(post_id=24, reason='spam')

# Positional arguments
def add_tags(post_id, *tags):
    pprint({'post_id': post_id, 'tags': tags})

add_tags(42, 'python', 'javascript', 'django')

# Keyword arguments
def create_post(**options):
    pprint(options)

create_post(
    title='Hello, World!', 
    content='This is our first post.',
    is_published=True,
)
create_post(
    title='Hello again!',
    content='This is our second post.',
)
```

**JavaScript**

```javascript
function report(post_id, reason='not-relevant') {
    console.log({post_id: post_id, reason: reason});
}

report(42);
report(post_id=24, reason='spam');

// Positional arguments
function add_tags(post_id, ...tags) {
    console.log({post_id: post_id, tags: tags});
}

add_tags(42, 'python', 'javascript', 'django');

// Keyword arguments
function create_post(options) {
    console.log(options);
}

create_post({
    'title': 'Hello, World!',
    'content': 'This is our first post.',
    'is_published': true
});
create_post({
    'title': 'Hello again!',
    'content': 'This is our second post.'
});
```

## Classes and inheritance

**Python**

```python
class Post(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return self.title

post = Post(42, 'Hello, World!')
isinstance(post, Post) == True
print(post)  # Hello, World!

# Inheritance
class Article(Post):
    def __init__(self, id, title, content):
        super(Article, self).__init__(id, title)
        self.content = content

class Link(Post):
    def __init__(self, id, title, url):
        super(Link, self).__init__(id, title)
        self.url = url

    def __str__(self):
        return '{} ({})'.format(
            super(Link, self).__str__(),
            self.url,
        )

article = Article(1, 'Hello, World!', 'This is my first article.')
link = Link(2, 'DjangoTricks', 'https://djangotricks.blogspot.com')
isinstance(article, Post) == True
isinstance(link, Post) == True
print(link)
# DjangoTricks (https://djangotricks.blogspot.com)
```

**JavaScript**

```javascript
class Post {
    constructor (id, title) {
        this.id = id;
        this.title = title;
    }
    toString() {
        return this.title;
    }
}

post = new Post(42, 'Hello, World!');
post instanceof Post === true;
console.log(post.toString());  // Hello, World!

// Inheritance
class Article extends Post {
    constructor (id, title, content) {
        super(id, title);
        this.content = content;
    }
}

class Link extends Post {
    constructor (id, title, url) {
        super(id, title);
        this.url = url;
    }
    toString() {
        return super.toString() + ' (' + this.url + ')';
    }
}

article = new Article(1, 'Hello, World!', 'This is my first article.');
link = new Link(2, 'DjangoTricks', 'https://djangotricks.blogspot.com');
article instanceof Post === true;
link instanceof Post === true;
console.log(link.toString());
// DjangoTricks (https://djangotricks.blogspot.com)
```

## Class properties: getters and setters

**Python**

```python
class Post(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self._slug = ''

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, value):
        self._slug = value

post = new Post(1, 'Hello, World!')
post.slug = 'hello-world'
print(post.slug)
```

**JavaScript**

```javascript
class Post {
    constructor (id, title) {
        this.id = id;
        this.title = title;
        this._slug = '';
    }

    set slug(value) {
        this._slug = value;
    }

    get slug() {
        return this._slug;
    }
}

post = new Post(1, 'Hello, World!');
post.slug = 'hello-world';
console.log(post.slug);
```