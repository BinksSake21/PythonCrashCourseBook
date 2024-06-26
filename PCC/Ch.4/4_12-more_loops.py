# All versions of foods.py in this section have avoided using for loops when printing, to save space.
# Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

my_foods.append('cannoli')
friend_food.append('ice cream')

print("My favorite foods are: ")
for my in my_foods:
    print(my.title())

print("\nMy friend's favorite foods are: ")
for friend in friend_food:
    print(friend.title())