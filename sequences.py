def sequence_class(immutable):
    '''Bind a class object'''
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls

# using condition expression to return the class type
def sequence_class_2(immutable):
    return tuple if immutable else list



# Produce a sequence class with the required characteristics.
# The create an instance of the class (t) by using the class object
# as a callable; i.e. calling the constructor
seq = sequence_class(immutable=True)
t = seq("Timbuktu")
# This is the same as doing tuple("Timbuktu"), but 'seq' is now
# dynamically typed
print(t)
print(type(t))
print('-------------------')

seq2 = sequence_class_2(immutable=True)
t2 = seq2("Nairobi")
print(t2)
print(type(t2))