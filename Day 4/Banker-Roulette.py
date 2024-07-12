import random
names_string = input("Please provide the names separated by ', '")
names = names_string.split(", ")
option = random.randint(0,len(names)-1)
print(f"{names[option]} is going to buy the meal today !")