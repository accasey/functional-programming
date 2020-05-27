# Functional Style Tools

Python's concept of iteration is simple and abstract. It is basically the idea that
you have a sequence of elements that can be accessed one at a time in order.

This high level of abstraction allows tools to be developed that work on iterables at 
an equally high level. Python provides a number of functions that serve as simple
building blocks for combining and working with iterables in sophisticated ways. 

Some people refer to this as 'functional style' Python.

## Map

This is probably one of the most widely recognised functional programming tools in Python.
At its core, map does a very simple thing.

Given a function and a sequence of objects, it calls the functions for every element
in the sequence producing a new sequence containing the return values of the function.
* In other words, we 'map' a function over a sequence to produce new values.

Example:
```python
map(ord, 'The quick brown fox')
```
This essentially says, for each element in the string call the function `ord`, with the 
element as an argument, and generate a new sequence comprising the return values aboard
in the same order as the input sequence.

Note that this returns a `map` object as the function performs 'lazy' evaluation.
i.e. it does not produce any output until it is needed.
* The `map` object will not call its function or access any elements from its input source until 
they are actually needed.
* This `map` object is itself an iterator object, and by iterating over it you can start
to produce output.
* You can use a `list()` or a `for` loop to iterate over the `map` object.

The `map()` function can be used with as many input sequences as your mapped function
needs.

If the function you provide to `map()` requires two arguments, then you need to provide
two input sequences to map. If the function requires three arguments, then you need
to provide three input sequences. 
* Generally you need to provide as many input sequences as there are arguments in the
`map()` function.
* For each output value that `map()` needs to produce it takes the next element from
each input sequence. 
* It then passes these, in orderm to the `map()` function, and the return value from
the funtion is the next output value from `map`.

```python
sizes = ['small', 'medium', 'large']
colours = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamader']
def combine(size, colour, animal):
    return f"{size} {colour} {animal}"

list(map(combine, sizes, colours, animals))
# ['small lavender koala', 'medium teal platypus', 'large burnt orange salamader']
```

If the input sequences are not all the same size, then the `map()` function will terminate
when the first input sequence is terminated (finished).

The `map()` function provides some of the same functionality as *comprehensions*.
These snippets all produce the same output, i.e. `['0', '1', '2', '3', '4']`.
```python
[str(i) for i in range(5)]
list(map(str, range(5)))
i = (str(i) for i in range(5)) # generator object
list(i)
i = map(str, range(5))  # a map object
list(i)
```

Either approach can be used, and there is no real clear choice which is better/faster etc.


## Reduce

As the name implies, the `filter()` function looks at each element of the sequence and
filters out (or removes) those which don't meet some criteria.

Like `map()`, `filter()` applies a predicate function to each element, and it also 
produces its results lazily.

However, unlike `map()`, `filter()` only accepts a single input sequence and the function
must accept only one argument.

The general form of `filter` takes a function of one argument as its first parameter, and
a sequence as its second parameter. It then returns an iterable object (of type `filter`)
and then applies its first argument to each element in the input sequence.

The sequence that the `filter` returns only contains only those elements of the input
for which the function returns `True`.

In the example below, the first argument is a lambda.
```python
positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
# <filter object at 0x7fcfd57fc340>
list(positives)
# [1, 6, 8]
```

If you pass `None` as the first argument to the `filter()`, it will filter out input
elements which evaluate to `False`.
* This is 'false-y' values, i.e. 0, empty lists, empty strings, False

```python
trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'Hello'])
list(trues)
# [1, True, [1, 2, 3], 'Hello']
```

Note that in Python 2, the `filter()` function is 'eager' and actually returns lists.

## Reduce
The `functools.reduce()` function repeatedly applies a function of two arguments to an
interim accumulator value and each element of the series in turn, updating or 
accumulating the interim value at each step with the result of the called function.
* The initial value of the accumulator can either be the first element of the sequence
or an optional supplied value (argument).

Ultimately, the final value of the accumulator is returned, thereby reducing the series
down to a single value.

```python
from functools import reduce
import operator

reduce(operator.add, [1, 2, 3, 4, 5])
# 15


# This is functionally equivalent to the code below
numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)

print(accumulator)
# 15
```

In the example below, you can see that the interim result is passed as the first
argument to the 'reducing' function, and then the next value in the input sequence
is passed as the second.

```python
from functools import reduce

def mul(x, y):
    print(f"mul {x} {y}")
    return x * y

reduce(mul, range(1, 10))
# mul 1 2
# mul 2 3
# mul 6 4
# mul 24 5
# mul 120 6
# mul 720 7
# mul 5040 8
# mul 40320 9
# 362880
```

Note:
* If you pass an empty sequence to reduce it will raise a type error.
* If you pass a sequence with one element, that element is returned without ever
calling the reducing function.