---
tags:
  - python
---

# Decorators

## Trace recursive functions

??? info "Reference"

    - [Python: trace recursive function](https://medium.com/@dizpers/python-trace-recursive-function-2be9ea546d84)
    - Lib [recursion-trace](https://pypi.org/project/recursion-trace/)
    - SO [How do I trace a recursive function with a return function in it](https://stackoverflow.com/questions/66712061/how-do-i-trace-a-recursive-function-with-a-return-function-in-it)

```python
from functools import wraps

# decorator to trace execution of recursive function
def trace(func):

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = '|  '

    # current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        print(f'{separator * (trace.recursion_depth + 1)}`-- return {result}')

        return result

    return traced_func
```

??? example

    ```python
    @trace
    def accumufact(n, fact=1) :
        if n == 1: return fact
        else: return accumufact(n-1, n*fact)

    @trace
    def fib(n):
        if n ==0 or n == 1: return n
        return fib(n-1) + fib(n-2)

    @trace
    def gcd(p, q):
        if q == 0: return p
        else: return gcd(q, p %q)


    def title(s):
        line = "-"*32
        print()
        print(line)
        print(s.center(32))
        print(line)
        print()

    title("accumufact")
    print(accumufact(7))

    title("fib")
    print(fib(4))

    title("gcd")
    print(gcd(165,27))
    ```

    **Output**:

    ```
    --------------------------------
            accumufact           
    --------------------------------

    |-- accumufact(7)
    |  |-- accumufact(6, 7)
    |  |  |-- accumufact(5, 42)
    |  |  |  |-- accumufact(4, 210)
    |  |  |  |  |-- accumufact(3, 840)
    |  |  |  |  |  |-- accumufact(2, 2520)
    |  |  |  |  |  |  |-- accumufact(1, 5040)
    |  |  |  |  |  |  |  `-- return 5040
    |  |  |  |  |  |  `-- return 5040
    |  |  |  |  |  `-- return 5040
    |  |  |  |  `-- return 5040
    |  |  |  `-- return 5040
    |  |  `-- return 5040
    |  `-- return 5040
    5040

    --------------------------------
                fib               
    --------------------------------

    |-- fib(4)
    |  |-- fib(3)
    |  |  |-- fib(2)
    |  |  |  |-- fib(1)
    |  |  |  |  `-- return 1
    |  |  |  |-- fib(0)
    |  |  |  |  `-- return 0
    |  |  |  `-- return 1
    |  |  |-- fib(1)
    |  |  |  `-- return 1
    |  |  `-- return 2
    |  |-- fib(2)
    |  |  |-- fib(1)
    |  |  |  `-- return 1
    |  |  |-- fib(0)
    |  |  |  `-- return 0
    |  |  `-- return 1
    |  `-- return 3
    3

    --------------------------------
                gcd               
    --------------------------------

    |-- gcd(165, 27)
    |  |-- gcd(27, 3)
    |  |  |-- gcd(3, 0)
    |  |  |  `-- return 3
    |  |  `-- return 3
    |  `-- return 3
    3
    ```