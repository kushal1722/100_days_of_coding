print("Welcome to the Water Park!")
height = int(input("What is your height? "))
if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5 for the ticket.")
    elif age <= 18:
        print("You have to pay $7 for the ticket.")
    else:
        print("You have to pay $12 for the ticket.")
else:
    print("You have to grow taller to ride roller coaster.")