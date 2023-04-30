# Markdown

## Basic syntax

See [Markdown Guide](https://www.markdownguide.org/basic-syntax/#code).

## Links at the bottom of the text

```markdown
[text](http://a.com)

[text][id]
⋮
[id]: http://b.org/ "title"
```

## Table with code blocks

Actually there is no simply solution and you should insert plain HTML table.

````
<table>
  <tr>
    <th>Python snippet</th>
  	<th>Ruby snippet</th>
  </tr>
  <tr>
<td>

```python
# Python 3: Fibonacci series up to n
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a < n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```
</td>
<td>

```ruby
# Output "I love Ruby"
say = "I love Ruby"
puts say

# Output "I *LOVE* RUBY"
say['love'] = "*love*"
puts say.upcase

# Output "I *love* Ruby"
# five times
5.times { puts say }
</td>
</tr>
</table>
````

<table>
  <tr>
    <th>Python snippet</th>
  	<th>Ruby snippet</th>
  </tr>
  <tr>
<td>

```python
# Python 3: Fibonacci series up to n
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a < n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```
</td>
<td>

```ruby
# Output "I love Ruby"
say = "I love Ruby"
puts say

# Output "I *LOVE* RUBY"
say['love'] = "*love*"
puts say.upcase

# Output "I *love* Ruby"
# five times
5.times { puts say }
```
</td>
</tr>
</table>

## Escape backticks `` ` `` in multiline code block

If you need to show extra backticks, enclose them with a higher number of them.

`````text
````
```python
print("Hello")
```
````
`````
