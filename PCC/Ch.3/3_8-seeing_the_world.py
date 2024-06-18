# Store the locations in a list. Make sure the list it not in alphabetical order.
locations = ['Tokyo', 'Seoul', 'Cambodia', 'Capcom HQ']

# Print your list in its original order. 
print("Here are the locations that I would like to visit: ")
print(locations)
print("\n")

# Use sorted() to print your list in alphabetical order without modifying the actual list. 
print("Here is the sorted list: ")
print(sorted(locations))
print("\n")

# Show that your list is still in its original order by printing it. 
print("Here is the original list: ")
print(locations)
print("\n")

# Use sorted() to pint you list in reverse-alphabetical order without changing the order of the original list. 
print("Here is the reverse sorted list: ")
print(sorted(locations, reverse=True))
print("\n")

# Show that your list is still in its original order by printing it again.
print("Here is the original list again: ")
print(locations)
print("\n")

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
locations.reverse()
print("Here is the permanent reverse list: ")
print(locations)
print("\n")

# Use reverse to change the order of your list again. Print the list to show it's back to its original order. 
locations.reverse()
print("Using the reverse function, here is the list: ")
print(locations)
print("\n")

# Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
locations.sort()
print("Using the sort function, here is the alphabetical list: ")
print(locations)
print("\n")

# Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed. 
locations.sort(reverse=True)
print("Using the sort reverse function, here is the reverse alphabetical list: ")
print(locations)
