# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each tests. Your code should look something like this:

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car =='audi'? I predict False.")
# print(car=='audi')

# Look closely at your results, and make sure you understand why each line evaluates True or False. 

# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evalue to False. 

# card_price = 500

# print("Variable card_price = 500.")

# print("Below are the 5 True evaluations.\n")

# print(f"Evaluation 1: card price == 500 is {card_price==500}. I predict True.\n")
# print(f"Evaluation 2: card price <= 500 is {card_price<=500}. I predict True.\n")
# print(f"Evaluation 3: card price => 500 is {card_price>=500}. I predict True.\n")
# print(f"Evaluation 4: card price >= 400 and card price <= 600 is {card_price>=400 and card_price<=600}. I predict True.\n")
# print(f"Evaluation 5: card price >= 400 or card price <= 600 is  {card_price==500}. I predict True.\n")



# print("Below are the 5 False evaluations.\n")

# print(f"Evaluation1: card price != 501 is {card_price != 501}. I predict False.\n")
# print(f"Evaluation 2: card price > 500 is {card_price > 500}. I predict False.\n")
# print(f"Evaluation 3: card price >= 600 is {card_price >= 600}. I predict False.\n")
# print(f"Evaluation 4: card price <= 400 or card price >= 600 is {card_price <= 400 or card_price>=600}. I predict False.\n")
# print(f"Evaluation 5: card price >= 600 or card price >=550 is {card_price >= 600 or card_price>=550}. I predict False.\n")

car = "subaru"

print("Is car=='subaru'? I predict True.")
print(car=='subaru')

print("\nIs car=='audi'? I predict False.")
print(car=='audi')

requested_toppings = 'onions'

if requested_toppings=='onions':
    print("\nIs requested_toppings=='onions? I predict True.")
    print(requested_toppings=='onions')

if requested_toppings!='mushrooms':
    print("\nIs requested_toppings=='mushrooms'? I predict False.")
    print(requested_toppings=='mushrooms')

age = '40'

print("\nIs age=='40'? I predict True.")
print(age=='40')

print("\nIs age=='20'? I predict False.")
print(age=='20')

answer = 25

if answer==25:
    print("\nIs answer==25? I predict True.")
    print(answer==25)

print("\nIs answer<=26? I predict True.")
print(answer<=26)

print("\nIs answer>=26? I predict False.")
print(answer>=26)

age_0 = 22
age_1 = 18

print("\nIs age_0>=21 and age_1>=21? I predict False.")
print(age_0>=21 and age_1>=21)

age_1 = 22

print("\nIs age_0>=21 and age_1>=21? I predict True.")
print(age_0>=21 and age_1>=22)

age_0 = 22
age_1 = 18

print("\nIs age_0>=21 or age_1>=21? I predict True.")
print(age_0>=21 or age_1>=21)

age_0 = 18

print("\nIs age_0>=21 or age_1>=21? I predict False.")
print(age_0>=21 or age_1>=21)