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

options = [rock, paper, scissors]

# Player Choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n "))
if user_choice < 0 or user_choice > 3:
    print("Invalid choice!")
else:
    print(options[user_choice])

    # Computer Choice
    computer_choice = random.randint(0, 2)
    print("Computer Chose:")
    print(options[computer_choice])

    # Game Logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
