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
