import random
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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
choice = int(input("What do you choose? TYpe 0 for Rock, 1 for Paper or 2 for Scissors"))
if choice == 0:
    print("You chose:")
    print(game_images[choice])
elif choice == 1:
    print("You chose:")
    print(game_images[choice])
elif choice == 2:
    print("You chose:")
    print(game_images[choice])
else:
    print("Wrong choice provided and you lose")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer chose:")
    print(game_images[computer_choice])
elif computer_choice == 1:
    print("Computer chose:")
    print(game_images[computer_choice])
else:
    print("Computer chose:")
    print(game_images[computer_choice])

if choice == 0:
    if computer_choice == 0:
        print("It's a tie")
    elif computer_choice == 1:
        print("You Lose")
    else:
        print("You Win")

if choice == 1:
    if computer_choice == 0:
        print("You Win")
    elif computer_choice == 1:
        print("It's a tie")
    else:
        print("You Lose")

if choice == 2:
    if computer_choice == 0:
        print("You Lose")
    elif computer_choice == 1:
        print("You Win")
    else:
        print("It's a tie")
