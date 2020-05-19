def hypervolume(*args):
    print(args)
    print(type(args))

    i = iter(args)
    v = next(i)
    for l in i:
        v *= l
    return v


print(hypervolume(3, 4))
print(hypervolume(3, 4, 5))