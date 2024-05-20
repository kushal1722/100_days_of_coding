# print("Welcome to the Water Park!")
# height = int(input("What is your height? "))
# bill = 0

# if height >= 120:
#     print("You can ride the roller coaster.")

#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("You have to pay $5 for the ticket.")
#     elif age <= 18:
#         bill = 7
#         print("You have to pay $7 for the ticket.")
#     else:
#         bill = 12
#         print("You have to pay $12 for the ticket.")

#     want_photo = input("Do you like to take a photo? Y or N: ")
#     if want_photo == "Y":
#         bill += 3

#     print(f"Your total bill is ${bill}")

# else:
#     print("You have to grow taller to ride roller coaster.")


# pizza example
print("Welcome to Domino's Pizza!")
size_of_pizza = input('What size would you prefer? "S", "M" or "L" ')
add_stuffing = input('Would you prefer extra stuffings? "Y" or "N" ')
add_cheese = input('Would you like to add cheese? "Y" or "N" ')

bill = 0
if size_of_pizza == "S":
    bill += 10
elif size_of_pizza == "M":
    bill += 15
else:
    bill += 20

if add_stuffing == "Y":
    if size_of_pizza == "S":
        bill += 3
    else:
        bill += 5

if add_cheese == "Y":
    if size_of_pizza == "S":
        bill += 1
    else:
        bill += 2

print(f"Your total bill will be: ${bill}")