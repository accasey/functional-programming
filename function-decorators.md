# Function Decorators

## Decorators
* Function decorators can add new bahviours to existing functions without 
modifying the decorated functions.
* You can implement decorators using any of the callable types of objects.
* You can apply multiple decorators to a function.


At a high level, decorators are a way to modify or enhance existing functions
in a non-intrusive and maintainable way.

In Python, a decorator is a callable object that takes in a callable and returns
a callable.
* You can think of this as 'Functions that take a function as an argument, and
return another function.'

When Python sees the decorator, it: 
1. Compiles the base function which produces a new function object.
1. Passes this function object to the decorator function.
    * Function decorators take a callable object as their only arugment and return 
a callable object as well.
1. Python takes the return value from the decorator and binds it to the name of
the original function.

So, in other words, decorators allow you to modify (replace or enhance) existing 
functions without changing those functions.

Callers of the original function do not have to change their code, because the 
decorator mechanism ensures that the same name is used for both the decorated 
and undecorated function.

Their example of a decorator function is that there is a requirement to ensure
the functions return ASCII characters. So rather than modifying every function
to use the ASCII function, which would be time consuming to implement (and to
remove possibly), you can do this with a decorator function.


## What can be a Decorator?

Functions are probably the most commonly used, but two other callable objects
are also used fairly commonly. The first of these is class objects.

### Classes as Decorators

1. Classes are **callable objects**.
1. Functions decorated with a class are replaced by an **instance of the class**.
1. These instances **must themselves be callable**.
    * So it must support the `__call__()` method.
    
 So you can decorate with a `class` as long as instances of the class implement
 `__call__()`.
 
 ## Multiple decorators
 
 You can enable multiple decorators, simply by listing each decorator on a separate line.
 ```python
@decorator1
@decorator2
@decorator3
def some_function()
    pass
```
 
They are processed in reverse order, so decorator3 before decorator2 etc.
The key point is that the result of decorator3 is passed to decorator2.
* The result of the final decorator is bound to the function
* The decorators do not need to know about the other decorators

You can also decorate a method in a class.


## Preserving Function Metadata
There are subtle problems with our use of decorators. We lose important metadata
from the original callable.
* Debugging tools and IDE's may use this info

The decorating replaces the original function with the decorator. This means that
the `__name__` and `__doc__` now reference the decorator.

Fortunately you can copy the `__name__` and `__doc__` from the wrapped function
to the wrapper function.

```python
def noop(f):
    def noop_wrapper():
        return f()
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper
```


Alternatively you can use the `functools.wraps()` to replace decorator metadata
with that of the decorated callable.
* This is itself a decorator, which you apply to your wrapper function.

```python
import functools
def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper
```


## Parameterised Decorators

An interesting and practical use for decorators is for validating function 
arguments. You might want to ensure that function arguments are within a 
range, or meet some other constraints.


