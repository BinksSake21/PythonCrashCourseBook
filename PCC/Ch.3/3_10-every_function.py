# Write a program that creates a list containing items and then uses each function introduced in this chapter at least once.
backlog_games = ['trails series: sky, zero, and steel', 'elden ring', 'nioh 2', 'persona 3 reload', 'persona 5 royal', 'monster hunter world', 'tales of arise', 'the witcher 3', 'wo long: fallen dynasty']

# Accessing Elements in a List
print("Accessing Elements in a List:\n")

print(f"Accessing element at index 0: {backlog_games[0]}\n")
print(f"Accessing element at index 1: {backlog_games[1]}\n")
print(f"Accessing element at index 2: {backlog_games[2]}\n")
print(f"Accessing element at index 3: {backlog_games[3]}\n")
print(f"Accessing element at index 4: {backlog_games[4]}\n")
print(f"Accessing element at index 5: {backlog_games[5]}\n")
print(f"Accessing element at index 6: {backlog_games[6]}\n")
print(f"Accessing element at index 7: {backlog_games[7]}\n")
print(f"Accessing element at index 8: {backlog_games[8]}")

print('------------------------------------\n')

# Index Positiions Start at 0, Not 1
print("Index Positions Start at 0, Not 1:\n")

print(f"First Index 0: {backlog_games[0].title()}\n")
print(f"Second Index 1: {backlog_games[1].title()}\n")
print(f"Third Index 2: {backlog_games[2].title()}\n")
print(f"Fourth Index 3: {backlog_games[3].title()}\n")
print(f"Fifth Index 4: {backlog_games[4].title()}\n")
print(f"Sixth Index 5: {backlog_games[5].title()}\n")
print(f"Seventh Index 6: {backlog_games[6].title()}\n")
print(f"Eighth Index 7: {backlog_games[7].title()}\n")
print(f"Ninth Index 8: {backlog_games[8].title()}")

print('------------------------------------\n')

# Using Individual Values from a List
print("Using Individual Values from a List: \n")

message = f"Currently playing: {backlog_games[5].title()}.\n"
print(message)

message = f"Next up is: {backlog_games[1].title()}.\n"
print(message)

message = f"Then the following: {backlog_games[2].title()}, {backlog_games[0].title()}, {backlog_games[3].title()}, {backlog_games[4].title()}, {backlog_games[6].title()}, {backlog_games[7].title()}, {backlog_games[8].title()}."
print(message)

print('-----------------------------------\n')

# Modifying Elements in a List
print("Modifying Elements in a List:\n")

print(f"Here is the current backlog_games list: {backlog_games}\n")

print("Adding cyberpunk to the backlog list:\n")

backlog_games[0] = 'cyberpunk'

print(f"Here is the updated backlog_games list: {backlog_games}.")

print('------------------------------------\n')

# Appending Element to the End of a List
print("Adding Elements to a List:\n")

print(f"Adding element 'trails series: sky, zero, and steel' to the backlog_games list.\n")
backlog_games.append('trails series: sky, zero, and steel')

print(f"Here is the updated backlog_games list: {backlog_games}.\n")

print("Creating a new list called more_games and appending elements to it.\n")
more_games = []
more_games.append('hell divers 2')
more_games.append('street fighter 6')
more_games.append('tekken 8')

print(f"Here is the more_games list: {more_games}.")

print('------------------------------------\n')

# Inserting Elements into a List
print("Inserting Elements into a List:\n")

print(f"Here is the current list of more_games: {more_games[0].title()}, {more_games[1].title()}, {more_games[2].title()}.\n")

print("Here are the following games to be inserted to the more_games list:\n")

more_games.insert(0, 'shin megami tensei v: vengeance')
more_games.insert(0, 'fatal fury: CoTW')
more_games.insert(0, 'ghost of tsushima')

print(f"Here is the updated list of more_games: {more_games[0].title()}, {more_games[1].title()}, {more_games[2].title()}, {more_games[3].title()}, {more_games[4].title()}, {more_games[5].title()}.")
print('------------------------------------\n')

# Removing Elements from a List
print("Removing Elements from a List:\n")

print(f"Here is the current backlog_games list: {backlog_games}.\n")

print(f"Removing element at index 0: {backlog_games[0]}.\n")
del backlog_games[0]

print(f"Here is the updated backlog_games list: {backlog_games}.\n")

print(f"Here is the current more_games list: {more_games}.\n")

print(f"Removing element at index 5: {more_games[0]}.\n")
del more_games[5]

print(f"Here is the updated more_games list: {more_games}.")

print('------------------------------------\n')

# Removing an Item Using the pop() Method
print("Removing an Item Using the pop() Method that removes the last item in a list.\n")

print("Using the pop() method to pop an element from backlog_games.\n")

print(f"Current backlog_games list: {backlog_games}.\n")
popped_backlog_games = backlog_games.pop()

print(f"Here is the updated backlog_games list after the pop() method: {backlog_games}.\n")

print("Using the pop() method again for the more_games list.\n")

print(f"Current more_games list: {more_games}.\n")
popped_more_games = more_games.pop()

print(f"Here is the updated more_games list after the pop() method: {more_games}.")

print('------------------------------------\n')

# Popping Items from Any Position in a List
print("Popping Items from Any Position in a List.\n")

print(f"Current backlog_games list: {backlog_games}.\n")

print(f"Using the pop() method on backlog_games list at index 3: {backlog_games[2]}.\n")
first_game_popped = backlog_games.pop(2)

print("Element at index 3: " + first_game_popped + " of backlog_games has been popped.\n")

print(f"Here is the updated backlog_games list: {backlog_games}.\n")

print(f"Current more_games list: {more_games}.\n")

print(f"Using the pop() method on backlog_games list at index 1: {more_games[1]}.\n")
second_game_popped = more_games.pop(1)

print("Element at index 3: " + second_game_popped + " of backlog_games has been popped.\n")

print(f"Here is the updated backlog_games list: {more_games}.")

print('------------------------------------\n')

# Removing an Item by Value

# Sorting a List Permanently with the sort() Method

# Sorting a List Temporarily with the sorted() Function

# Printing a List in Reverse Order

# Finding the Length of a List
# print("Finding the Length of a List: \n")

# print(f"Here is the length of the list: {len(backlog_games)}.\n")

# print('------------------------------------')

