# list of people to invite
guest_list = ['bruce lee', 'akira toriyama', 'eiichiro oda']

# print invitation
print(f"Hello {guest_list[0].title()}, would you like to join me for dinner?\n")
print(f"Hello {guest_list[1].title()}, would you like to join me for dinner?\n")
print(f"Hello {guest_list[2].title()}, would you like to join me for dinner?\n")

print("---------------------------------------------")
# Add a print() call at the end of your program, stating the name of the guest who can't make it.
declined_invitation = 'bruce lee'
guest_list.remove(declined_invitation)

print(f"{declined_invitation.title()} cannot make it.\n")

print("---------------------------------------------")

# Modify your list, replacing the name of the guest who can't make it with the name of the
# new person you are inviting. 

guest_list.insert(0, 'gege akutami')

# Print a second set of invitation messages, one for each person who is still on your list. 

print(f"Hello {guest_list[0].title()}, would you like to join me for dinner?\n")
print(f"Hello {guest_list[1].title()}, would you like to join me for dinner?\n")
print(f"Hello {guest_list[2].title()}, would you like to join me for dinner?\n")

print("---------------------------------------------")

# Add a print() call to the end of your program, informing people that you found a bigger table.
print(f"Hello {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, I found a bigger table and will invite more people to join us for dinner.\n")

print("---------------------------------------------")

# Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, 'monkey d. luffy')

# Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, 'gojo satoru')

# Use append() to add one new guest to the end of your list.
guest_list.append('yuji itadori')

print(f"Hi {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, {guest_list[3].title()}, {guest_list[4].title()}, {guest_list[5].title()}, I found a bigger table, would you like to join for dinner?\n")

print("---------------------------------------------")

# Add a new line that prints a message saying that you can invite only two people for dinner. 

print(f"Sorry {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, {guest_list[3].title()}, {guest_list[4].title()}, {guest_list[5].title()}, the bigger table will not be ready in time, and now I only have space for two guests.\n")

# Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't intie them to dinner. 

guest_pop = guest_list.pop()
print(f"Hi {guest_pop.title()}, Sorry the bigger table is unavailable. Let's get together another time.\n")

guest_pop = guest_list.pop()
print(f"Hi {guest_pop.title()}, Sorry the bigger table is unavailable. Let's get together another time.\n")

guest_pop = guest_list.pop()
print(f"Hi {guest_pop.title()}, Sorry the bigger table is unavailable. Let's get together another time.\n")

guest_pop = guest_list.pop()
print(f"Hi {guest_pop.title()}, Sorry the bigger table is unavailable. Let's get together another time.\n")

print("---------------------------------------------")

# Print a message to each of the two people still on your list, letting them know they're still invited.

print(f"Hi {guest_list[0].title()}, you are still invited to dinner.\n")

print(f"Hi {guest_list[1].title()}, you are still invited to dinner.\n")

# Use del to remove the last two names from your list, so you have an empty list.

del guest_list[0]
del guest_list[0]

print("---------------------------------------------")

# Print you list to make sure you actually have an empty list at the end of your program.

print(f"Guest list {guest_list} is now empty.")

