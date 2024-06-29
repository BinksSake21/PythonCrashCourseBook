# Start with your program from Exercise 4-1. 


# Store three kinds of your favorite pizzas in a list. 
favorite_pizzas = [
    'pepperoni', 'meat lovers', 'supreme'
    ]

# Use a for loop to print the name of each pizza. Modify your for loop 
# to print a sentence using the name of a pizza.
for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")

# Add a line at the end of your program, outside the for loop, that 
# states how much you like pizza.
print("I really love pizza!\n")

# Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following: 
friend_pizza = favorite_pizzas[:]

# Add a new pizza to the original list. 
favorite_pizzas.append('extra cheese')

# Add a different pizza to the list friend_pizza.
friend_pizza.append('veggie lovers')

# Prove that you have two separate lists. Print the message My favorite 
# pizzas are:, then use a for loop to print the first list. 
print(f"My favorite pizzas are: ")

for fav_pizza in favorite_pizzas:
    print(fav_pizza.title())

print(f"\nMy friend's favorite pizzas are: ")

for friend in friend_pizza:
    print(friend.title())

# Print the message My friend's favorite pizzas are:, then use a for 
# loop to print the second list. Make sure each new pizza is stored 
# in the appropriate list. 
