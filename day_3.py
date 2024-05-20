print("Welcome to the Water Park!")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")

    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("You have to pay $5 for the ticket.")
    elif age <= 18:
        bill = 7
        print("You have to pay $7 for the ticket.")
    else:
        bill = 12
        print("You have to pay $12 for the ticket.")

    want_photo = input("Do you like to take a photo? Y or N: ")
    if want_photo == "Y":
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("You have to grow taller to ride roller coaster.")