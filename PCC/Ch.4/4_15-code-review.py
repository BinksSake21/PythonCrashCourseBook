# Choose three of the programs you've written in this chapter and modify
# each one to comply with PEP 8.

# Use four spaces for each indentation level. Set your text editor to 
# insert four spaces every time you press the TAB key, if you haven't
# already done so (see Appendix B for instructions on how to do this.)

# Use less than 80 characters on each line, and set your editor to show
# a vertical guideline at the 80th character position.

# Don't use blank lines excessively in your program files. 

# 4_11-my_pizzas_your_pizzas.py

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

# 4_12-more_loops.py

# All versions of foods.py in this section have avoided using for loops 
# when printing, to save space.
# Choose a version of foods.py, and write two for loops to print each 
# list of foods.

my_foods = [
    'pizza', 'falafel', 'carrot cake'
    ]

friend_food = my_foods[:]

my_foods.append('cannoli')

friend_food.append('ice cream')

print("My favorite foods are: ")
for my in my_foods:
    print(my.title())

print("\nMy friend's favorite foods are: ")
for friend in friend_food:
    print(friend.title())

# 4_13-buffet.py

# A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.

buffet_food = (
    'crab legs', 'walnut shrimp', 'beef broccoli', 
    'fried rice', 'stirfried clams'
    )

# Use a for loop to print each food the restaurant offers.
print("Here is the menu:")

for foods in buffet_food:
    print(foods.title())

# Try to modify one of the items, and make sure that Python rejects 
# the change.

# buffet_food[0] = 'crawfish'

# The restaurant changes its menu, replacing two of the items with 
# different foods. Add a line that rewrites the tuple, and then use a 
# for loop to print each of the items on the revised menu.
buffet_food = (
    'crawfish', 'beef teriyaki', 'beef broccoli', 
    'fried rice', 'stirfried clams'
    )

print("\nWe replaced two items on the menu:")

for foods in buffet_food:
    print(foods.title())
