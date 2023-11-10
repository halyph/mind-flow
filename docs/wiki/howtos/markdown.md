---
tags:
  - markdown
---

# Markdown

## README samples

- [stkeky/best-of-scala](https://github.com/stkeky/best-of-scala/blob/main/README.md) A ranked list of awesome Scala projects. It is based on [best-of-lists/best-of-generator](https://github.com/best-of-lists/best-of-generator).

## Basic syntax

See [Markdown Guide](https://www.markdownguide.org/basic-syntax/#code).

## Collapsed text

See details [HTML Details Element `<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details).


!!! example

    <div class="result">
    <details>
    <summary>
    <b><a href="https://github.com/sbt/sbt">sbt</a></b> (🥇33 ·  ⭐ 4.7K) - sbt, the interactive build tool. 
    <code>
      <a href="http://bit.ly/3nYMfla">Apache-2</a>
    </code>
    <code>
      [MIT](http://bit.ly/34MBwT8)
    </code>
    <code>
      <img src="https://scalac.io/wp-content/uploads/2021/02/image-125-1.svg" style="display:inline;" width="13" height="13">
    </code>
    </summary>

    - [GitHub](https://github.com/sbt/sbt) (👨‍💻 410 · 🔀 920 · 📥 12M · 📋 4.1K - 18% open · ⏱️ 02.11.2023):

      ```
      git clone https://github.com/sbt/sbt
      ```
    </details>
    </div>


??? note "Markdown"

    ````
    ```markdown
    <details>
    <summary>
    <b><a href="https://github.com/sbt/sbt">sbt</a></b> (🥇33 ·  ⭐ 4.7K) - sbt, the interactive build tool. 
    <code>
      <a href="http://bit.ly/3nYMfla">Apache-2</a>
    </code>
    <code>
      [MIT](http://bit.ly/34MBwT8)
    </code>
    <code>
      <img src="https://scalac.io/wp-content/uploads/2021/02/image-125-1.svg" style="display:inline;" width="13" height="13">
    </code>
    </summary>

    - [GitHub](https://github.com/sbt/sbt) (👨‍💻 410 · 🔀 920 · 📥 12M · 📋 4.1K - 18% open · ⏱️ 02.11.2023):

      ```
      git clone https://github.com/sbt/sbt
      ```
    </details>
    ```
    ````

## Links at the bottom of the text

```markdown title="Markdown"
[text](http://a.com)

[text][id]
⋮
[id]: http://b.org/ "title"
```

## Table with code blocks

Actually there is no simple solution and you should insert plain HTML table.

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

??? note "Markdown"

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
    ````

## Escape backticks `` ` `` in multiline code block

If you need to show extra backticks, enclose them with a higher number of them.

`````markdown title="Markdown"
````
```python
print("Hello")
```
````
`````
