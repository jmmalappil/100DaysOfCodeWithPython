print("The Love Calculator is calculating your score...")
name1 = input("Please provide the first name:")
name2 = input("Please provide the second name:")

combine_names = name1 + name2
lower_names = combine_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = t + r + u + e

score = str(first_digit) + str(second_digit)
love_score = int(score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score >=40 and (love_score <= 50)):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")