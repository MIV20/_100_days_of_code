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

game_images = [rock, paper, scissors]

turn = int(input("Ready for some rock, paper, scissors? Select 0 for rock, 1 for paper or 2 for scissors.\n"))



if turn >= 3 or turn < 0:
    print("You chose an invalid response. YOU LOSE!")
else:
    print(game_images[turn])
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if turn == 0 and computer_choice == 2:
        print("YOU WIN!")
    elif turn == 2 and computer_choice == 0:
        print("YOU LOSE!")
    elif turn > computer_choice:
        print("YOU WIN!")
    elif computer_choice > turn or turn == 2 and computer_choice == 0:
        print("YOU LOSE!")
    elif turn == computer_choice:
        print("DRAW")
