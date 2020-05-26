# Closures

## Local Functions
The keyword `def` is used to define new functions. 
It essentially binds the body of a function to a name, in
such a way that functions are simply objects like everything else
in Python.

It is important to remember that `def` is executed at runtime, so functions
are defined at runtime.

You can also define functions inside other functions.
* These functions are referred to as local functions, 
as they are defined local to a specific function's scope.
* Local functions are also defined when `def` is executed at runtime.
Therefore each time the function is called, a new copy is made.

Local functions are not 'members' of their enclosing functions.

In the example below, the `last_letter` function is local to
the `sort_by_last_letter` function.
```python
def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

sort_by_last_letter(['hello','from','a','local','function'])
# ['a', 'local', 'from', 'function', 'hello']

last_letter('Andrew')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'last_letter' is not defined
```

### Scoping
Local functions are subject to the same scoping rules are regular functions.
1. **L**ocal
2. **E**nclosing
3. **G**lobal
3. **B**uilt-in

### Uses
* One off specialised functions, e.g. creating sorting key functions.
* Code organisation and readability.
* Similar to lambdas.
* More general than lambdas though, e.g. they can contain multiple expressions, and contain statements such as `import`.


### First-class functions
Functions can be passed to and returned from functions.

More generally, they can be treated like any other data.

They are a powerful concept that becomes even more powerful when combined with closures.

### Function Factories

These functions are functions that return other functions, where the returned functions
are specialised in some way based on arguments to the factory.
* The factory function takes some arguments.
* It then creates a local function which takes its own arguments, but also uses the arguments passed to the factory.


The combination of runtime function defintion, and closures makes this possible.


In the local function below the exponent (passed into the factory function) stores the
exponent in the local closure. That way when the square/cube function is invoked it
remembers the exponent it was created with.
```python
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


square = raise_to(2)
square(5)
# 25
cube = raise_to(3)
cube(3)
# 27
```


### Binding names in enclosing scopes
Like the `global` keyword, python has a `nonlocal` keyword which allows you to,
 in the local function, override the variable from the enclosing function. Or you
can use the variable from the enclosing scope within the local function/scope.
* Note that the variable must exist in the enclosing namespace, otherwise a `SyntaxError` will be thrown.
 