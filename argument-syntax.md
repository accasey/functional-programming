# Argument syntax
These rules apply also to lambda functions.

## Arbitrary positional arguments
Typically `*args` is used, but this is by convention.
* Colloquially called 'star args'
* `*args` is passed as a tuple
* Must come after any normal positional arguments
* There can only be one occurrence of a 'star' argument
* Only accepts positional arguments
* Must come after regular arguments
* Any regular arguments after `*args` must be passed as key word arguments
* Mandatory arguments must also be specified before any optional arguments
    * i.e. where there is a default value supplied

## Arbitrary keyword arguments
You prefix the variable/argument with `**` to accept arbitrary keyword arguments.
* Can be accepted by callables
* Conventionally called `**kwargs`
* `**kwargs` is passed as a dictionary
    * each key is the dictionary key
* Many examples of this, e.g. `print` or `str.format()`
* `*args` must come before `**kwargs`
* `**kwargs` must be last in the argument list


## Positional-only arguments
* You include a forward slash in your argument list
    ```python
    def number_length(x, /):
      return len(str(x))
    ```
* If you try to pass them with a keyword, it will generate a `TypeError`
    * `TypeError: number_length() got some positional-only arguments passed as keyword arguments: x`

### Why positional-only arguments 
* This provides parity with other languages, e.g. c, which use position only arguments.
* They prevent formal argument names from becoming part of the API
    * This prevents dependencies on the names
    * Useful when the names have no semantic meaning
    

## Extended Call Syntax


```python
def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (11, 12, 13, 14, 15)
print(type(t))
# <class 'tuple'>
print_args(*t)
# 11
# 12
# (13, 14, 15)
```

```python
def color(red, green, blue, **kwargs):
    print('r =', red)
    print('g =', green)
    print('b =', blue)
    print(kwargs)

k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
print(type(k))
# <class 'dict'>
color(**k)
# r = 21
# g = 68
# b = 120
# {'alpha': 52}
```

The `dict()` function uses `**kwargs`` in its initialiser.
```python
k = dict(red=21, green=68, blue=120, alpha=52)
color(**k)
# r = 21
# g = 68
# b = 120
# {'alpha': 52}
```
