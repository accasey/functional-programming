def trace(f, *args, **kwargs):
    print('args =', args)
    print('kwargs =', kwargs)
    result = f(*args, **kwargs)
    print('result =', result)
    return result

print(type(int()))
trace(int, 'ff', base=16)
print(int('ff', base=16))