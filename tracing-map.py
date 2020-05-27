class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)

        return wrap


result = map(Trace()(ord), 'The quick brown fox')
print(result)
for o in result:
    print(o)

print(list(result))