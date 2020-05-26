def escape_unicode(f):
    '''The only argument, f, is the function to be decorated.'''

    def wrap(*args, **kwargs):
        '''This is the important bit, and it uses *args and *kwargs to accept
        any number of arguments, and then calls the f. It takes its return value
        and then runs ascii to convert the characters to ascii.'''
        x = f(*args, **kwargs)
        return ascii(x)

    # Need to return the callable object as well
    return wrap


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix


@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'


# Now wehn we make norwegian island names, the name will be properly
# escaped, and the tracer will record the call.
print(norwegian_island_maker('Llama'))
print(norwegian_island_maker('Python'))
print(norwegian_island_maker('Troll'))
tracer.enabled = False
print('Setting the tracing off')
print(norwegian_island_maker('Llama'))
print(norwegian_island_maker('Python'))
print(norwegian_island_maker('Troll'))


print('Calling the decorator from a class method...')
tracer.enabled = True
im = IslandMaker(" Island")
print(im.make_island("Python"))
print(im.make_island("Llama"))