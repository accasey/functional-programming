def check_non_negative(index):
    """This returns the nested validator function """
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(f'Argument {index} must be non-negative')
            return f(*args)

        return wrap

    # The validator function is the actual decorator
    return validator


# This actually calls check_non_negative
@check_non_negative(1)
def create_list(value, size):
    return [value] * size


print(create_list('a', 3))
print(create_list(123, -6))



# Technically the check_non_negative function is not a decorator, as
# a decorator is a callable object that takes a callable object as an
# argument and returns a callable object.
