# water park example.
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

# ---------------------------------------------------------------------------------------------------
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



# ---------------------------------------------------------------------------------------------------
# Treasure hunt
print("Welcome to treasure hunt!!!")
print("Your mission is to find the treasure!")
choice1 = input('You\'re at the crossroad. Where do you want to go? "Left" or "Right"\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve arrived at the sea shore. Type "Wait" for the boat or type "Swim" to swim across the sea.\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve arrived at the final destination. There are three doors "Yellow", "Blue" and "Red". One contains the treasure. Which one do you choose?\n').lower()
        if choice3 == "yellow":
            print("It\'s room full of fire. You lost...")
        elif choice3 == "red":
            print("BINGOOOOO! YOU\'VE FOUND THE TREASURE! THE ONE PIECE U!!!!")
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____/
______/______/______/______/______/______/______/______/______/______/
********************************************************************************''')
        elif choice3 == "blue":
            print("It\'s room full of beasts. You lose...")
        else:
            print("You\'ve choose the wrong option. Game over...")
    else:
        print("You got attacked by a shark. Game Over...")
else:
    print("You fell into a hole. Game Over...")