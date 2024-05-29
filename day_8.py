# FUNCTIONS
# def greet():
#     print("Hello world!")
#     print("Hello world!")
#     print("Hello world!")
# greet()

# FUNCTION WITH ARGUMENTS AND PARAMETERS
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
# greet_with_name("Kushal")

# FUNCTIONS WITH MORE THAN 1 INPUT
# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"Are you in {location} right now?")
# greet_with_name("Kushal", "Tirupati")

# FUNCTIONS WITH MORE THAN 1 INPUT USING KEYWORD ARGUMENTS
# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"Are you in {location} right now?")
# greet_with_name(location = "Tirupati", name = "Kushal")



#                               CAESAR CIPHER PROJECT

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decode:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# ENCRYPT
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabets[new_position]
    print(f"The encoded text is: {cipher_text}")

# DECRYPT
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        plain_text += alphabets[new_position]
    print(f"The decrypted text is: {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)