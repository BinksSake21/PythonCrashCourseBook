# A number raised to the third power is called a cube. Ex: 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cuber of each integer from 1 through 10)
cubes = []

# Use a for loop to print out the value of each cube.
for cube in range(1, 11):
    cubes.append(cube**3)

print(cubes)
