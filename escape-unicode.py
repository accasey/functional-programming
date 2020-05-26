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

@escape_unicode
def northern_city():
    return 'Tromsø'

print(northern_city())