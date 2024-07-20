from art import logo
import random
print(logo)

def guess(num, attempts):
    chances = 0
    while chances < attempts:
        guess_num = int(input("Make a guess:"))
        if guess_num < num:
            print("Too Low.")
            print("Guess again.")
        elif guess_num > num:
            print("Too High")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {num}")
            break
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
    guess(number, attempts)

elif difficulty == 'hard':
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
    guess(number, attempts)

else:
    print("You have entered a wrong choice")
