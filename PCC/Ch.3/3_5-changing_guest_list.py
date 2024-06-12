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