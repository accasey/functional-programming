# List
l = [i * 2 for i in range(10)]
grid = [(x,y) for x in range(5) for y in range(5)] # List of Tuples
values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0] # With 'if'
vals = [[y * 3 for y in range(x)] for x in range(10)] # Nested comprehension

# Dict
d = {i: i * 2 for i in range(10)}

# Set
s = {i for i in range(10)}
x1 = {x * y for x in range(10) for y in range(10)}

# Generator
g = (i for i in range(10))
g1 = ((x, y) for x in range(10) for y in range(10))