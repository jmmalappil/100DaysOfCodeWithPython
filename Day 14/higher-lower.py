import art
import random
import os
import game_data as gd
print(art.logo)

def clear_screen():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    # Check if the system is Unix-like
    else:
        os.system('clear')

# Create a function to generate a random item from game_data and print it
def choice_data(data, id):
    choice = random.choice(data)
    print(f"Compare {id}: {choice['name']}, a {choice['description']}, from {choice['country']}")
    return choice

#
def compare(choiceA, choiceB):
    guess_right = False
    choice={}
    response = input("Who has more followers? Type 'A' or 'B':")
    if response == 'A':
        if choiceA['follower_count'] > choiceB['follower_count']:
            guess_right = True
            choice=choiceA
    if response == 'B':
        if choiceB['follower_count'] > choiceA['follower_count']:
            guess_right = True
            choice = choiceB
    return choice, guess_right


choice_A = choice_data(gd.data, 'A')

print(art.vs)

choice_B = choice_data(gd.data, 'B')

choice, guess = compare(choice_A, choice_B)

score = 0

is_continue = True

while is_continue:

    if guess:
        score += 1
        clear_screen()
        print(art.logo)
        print(f"You're right! Current score: {score}")
        print(f"Compare A: {choice['name']}, a {choice['description']}, from {choice['country']}")

        print(art.vs)

        choice_B = choice_data(gd.data, 'B')

        choice, guess = compare(choice, choice_B)

    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        is_continue = False



