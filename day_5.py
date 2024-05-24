# list = ['fruit', 'mango', 'watermelon']
# for lists in list:
#     print(lists)

# name = int(input("select no: "))
# for n in range(1, name + 1):
#     print(n)
# # print(name)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '!', '#', '$', '%', '*', '(', ')']

print("Welcome to the passcode generator!")
no_of_letters = int(input("How many letters would you like?: "))
no_of_numbers = int(input("How many numbers would you like?: "))
no_of_symbols = int(input("How many symbols would you like?: "))

passcode_list = []
for char in range(1, no_of_letters + 1):
    passcode_list += random.choice(letters)
for char in range(1, no_of_numbers + 1):
    passcode_list += random.choice(numbers)
for char in range(1, no_of_symbols + 1):
    passcode_list += random.choice(symbols)

random.shuffle(passcode_list)
password = ""
for char in passcode_list:
    password += char

print(f"Your final password is: {password}")