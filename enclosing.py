message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # global message
        # nonlocal message
        message = 'local'


    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosing()
print('global message:', message)
