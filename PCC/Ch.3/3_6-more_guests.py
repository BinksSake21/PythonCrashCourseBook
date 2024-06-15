# list of people to invite
guest_list = ['bruce lee', 'akira toriyama', 'eiichiro oda']

# print invitation
print(f"Hello {guest_list[0].title()}, would you like to join me for dinner?")
print(f"Hello {guest_list[1].title()}, would you like to join me for dinner?")
print(f"Hello {guest_list[2].title()}, would you like to join me for dinner?")
print("\n")

# Add a print() call at the end of your program, stating the name of the guest who can't make it.
declined_invitation = 'bruce lee'
guest_list.remove(declined_invitation)

print(f"{declined_invitation.title()} cannot make it.\n")

# Modify your list, replacing the name of the guest who can't make it with the name of the
# new person you are inviting. 

guest_list.insert(0, 'gege akutami')

# Print a second set of invitation messages, one for each person who is still on your list. 

print(f"Hello {guest_list[0].title()}, would you like to join me for dinner?")
print(f"Hello {guest_list[1].title()}, would you like to join me for dinner?")
print(f"Hello {guest_list[2].title()}, would you like to join me for dinner?")
print("\n")

# Add a print() call to the end of your program, informing people that you found a bigger table.
print(f"Hello {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, I found a bigger table and will invite more people to join us for dinner.\n")

# Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, 'monkey d. luffy')

# Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, 'gojo satoru')

# Use append() to add one new guest to the end of your list.
guest_list.append('yuji itadori')

print(f"Hi {guest_list[0].title()}, I found a bigger table, would you like to join for dinner?\n")
print(f"Hi {guest_list[1].title()}, I found a bigger table, would you like to join for dinner?\n")
print(f"Hi {guest_list[2].title()}, I found a bigger table, would you like to join for dinner?\n")
print(f"Hi {guest_list[3].title()}, I found a bigger table, would you like to join for dinner?\n")
print(f"Hi {guest_list[4].title()}, I found a bigger table, would you like to join for dinner?\n")
print(f"Hi {guest_list[5].title()}, I found a bigger table, would you like to join for dinner?\n")
