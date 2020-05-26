class CallCount():
    def __init__(self, f):
        self.f = f  # this is the function passed in
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print(f"Hello {name}!")


print(hello("Fred"))
print(hello("Wilma"))
print(hello("Barney"))
print(hello("Betty"))

print("Count:", hello.count)