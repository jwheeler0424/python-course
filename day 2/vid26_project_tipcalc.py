# Day 2 video 26 Project - Tip Calculator

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12,or 15? ")) / 100
people = int(input("How many people to split the bill? "))

tip = bill * tip_percent

total_bill = bill + tip
person_bill = round(total_bill / people, 2)
person_bill = "{:.2f}".format(person_bill)

print(f"Each person should pay: ${person_bill}")