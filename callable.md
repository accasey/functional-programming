# Callables

Since callable instances are just normal class instances, their classes can 
define any other methods that you want.

```python
from resolver import Resolver
resolve('sixty-north.com')
# is the same as
resolve.__call__('sixty-north.com')
```
```python
from timeit import timeit
timeit(setup="from __main__ import resolve", stmt="resolve('google.com')", number=1)
# 0.005561599999964528
timeit(setup="from __main__ import resolve", stmt="resolve('google.com')", number=1)
# 4.300000000512227e-06
```

## Classes
Everything in Python is an object, including classes.

Class objects and instance objects produced from those classes are very 
different things.

The `class` keyword binds a class object to a named reference.

Constructor calls are made by calling the class object.
* Arguments passed to the class object are forwarded to the class's `__init__()` 
method.
    * if a `__init__()` method has been defined

### Classes Are Object Factories

In essence, the class object callable is a factory function which, when invoked,
 produced new instances of that class.
* Classes **produce new instances** when they are invoked.


## Lambdas
These are simple callable objects, can be passed directly to a function without
 the overhead of the `def` statement and the code block it introduces.
* In many cases it is not necessary for the callable object to be bound to a name.
* If it is being passed directly to a function, then an anonymous callable 
function would suffice.

Use `lambda` with care to avoid creating inscrutable code.
* Excessive use of lambdas can obfuscate rather than clarify code.

<p><small>Example</small></p>

```Python
# name is the single argument to the lambda
scientists = ['Marie Curie','Albert Einstein','Rosalind Franklin','Niels Bohr'
,'Dian Fossey','Isaac Newton','Grace Hopper','Charles Darwin','Lise Meitner']
sorted(scientists, key=lambda name: name.split()[-1])
# ['Niels Bohr', 'Marie Curie', 'Charles Darwin', 'Albert Einstein', 
# 'Dian Fossey', 'Rosalind Franklin', 'Grace Hopper', 'Lise Meitner', 
# 'Isaac Newton']

'Marie Curie'.split()
# ['Marie', 'Curie']
'Marie Curie'.split()[-1]
# 'Curie
```

Lambda itself is an expression that results in a callable object.
You can see this by binding the result of the lambda expression to 
a named expression using assignment. 
* It is callable like a function.
* Keep your lambda's simple enough that they are obviously correct by inspection.

```python
last_name = lambda name: name.split()[-1]
print(last_name)
# <function <lambda> at 0x000002305B1ADCA0>
last_name("Andrew Casey")
# 'Casey'
```
### Comparison between functions and lambdas
| def name(args): body  |  lamda args: expr |
|---|---|
| Statement which defines a function and binds it to a name  |  Expression which evaluates to a function |
| Must have a name  | Anonymous  |
| Arguments are delimited by parentheses, separated by commas  | Argument list terminated by a colon, separated by commas  |
| Zero or more arguments are supported - zero arguments => () | Zero or more arguments supported - zero arguments => lambda: |
| The body is an indented block of statements | The body is a single expression |
| A return statement is required to return anything other than `none` | The return value is given by the body; no `return` statement is permitted |
| Can have docstrings | Cannot have docstrings | 
| Easy to access for testing | Awkward or impossible to test |


## Callable objects
The following are callable:
1. Regular functions
    ```python
    def is_even(x):
       return x % 2 == 0
   
    callable(is_even)
    # True
    ```
1. Lambda expressions
    ```python
    is_odd = lambda x: x % 2 == 1
   
    callable(is_odd)
    # True
    ```
1. Class objects are callable (this invokes the constructor)
    ```python
    callable(list)
    # True
    ```
1. Methods are callable.
    ```python
    callable(list.append)
    # True
    ```
1. Instance objects can be made callable by defining the `__call__(self):` method
    ```python
    class CallMe():
       def __call__(self):
           print("Called!")
   
    my_call_me = CallMe()
    callable(my_call_me)
    # True
    ```

But many objects, such as string instances, are not callable.
```python
callable("This is not callable")
# False
```