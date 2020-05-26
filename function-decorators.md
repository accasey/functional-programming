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
 