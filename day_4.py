import random
# random_int = random.randint(1, 10)
# print(random_int)
# random_float = random.random()
# print(random_float)
# heads_or_tails = random.randint(0, 1)
# if heads_or_tails == 1:
#     print("Heads it is!")
# else:
#     print("Tails it is!")

# lists
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor] 
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissor.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You've choosen the invalid option.")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chooses:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")   
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif computer_choice == 2 and user_choice == 1:
        print("You lose")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice == 1 and user_choice == 0:
        print("You lose")
    elif computer_choice == user_choice or user_choice == computer_choice:
        print("It's a draw!")
    # else:
    #     print("You've choosen the invalid option.")
