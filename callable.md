# Callables

Since callable instances are just normal class instances, their classes can define any other methods that you want.

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

Class objects and instance objects produced from those classes are very different things.

The `class` keyword binds a class object to a named reference.

Constructor calls are made by calling the class object.
* Arguments passed to the class object are forwarded to the class's `__init__()` method.
    * if a `__init__()` method has been defined

### Classes Are Object Factories

In essence, the class object callable is a factory function which, when invoked, produced new instances of that class.
* Classes **produce new instances** when they are invoked.
* The internal Python machinery for 