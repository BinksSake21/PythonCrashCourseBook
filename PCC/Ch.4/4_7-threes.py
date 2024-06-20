# Make a list of the multiples of 3, from 3 to 30.
threes = list(range(1, 11))

# Use a for loop to print the numbers in your list.
print("Using a for loop for range 1 to 10 and multiply by 3:")
for three in threes:
    print(three * 3)

# Online solution
print("\nOnline solution:")
threes = list(range(3, 31, 3))

for number in threes:
    print(number)