#Video 37 - Day 3 Interactive Coding Exercise - Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
true_score = str(name1.count("t") + name2.count("t") + name1.count("r") + name2.count("r") + name1.count("u") + name2.count("u") + name1.count("e") + name2.count("e"))
love_score = str(name1.count("l") + name2.count("l") + name1.count("o") + name2.count("o") + name1.count("v") + name2.count("v") + name1.count("e") + name2.count("e"))
total_score = int(true_score + love_score)

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")