# height = input("What is your height? ")
# weight = input("What is your weight? ")
# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = weight_as_int / height_as_float ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

#f-strings
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height}, your winning is {isWinning}")

# example
# age = input("Please enter your age: ")
# print(f"Your age is {age}")
# years = 90 - int(age)
# weeks = years * 52
# print(f"You have {weeks} weeks left.")

# Tip calculator
print("Welcome to tip calculator project!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much % would you like to tip 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)
print(f"Each person should pay: ${final_bill}")