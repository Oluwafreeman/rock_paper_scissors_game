import random

# num = random.randint(0,1)
# if num == 0:
#     print("Tail")
# else:
#     print("Head")

# row1 = ["⬜","⬜","⬜"]
# row2 = ["⬜","⬜","⬜"]
# row3 = ["⬜","⬜","⬜"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# vertical = int(position[0])
# horizontal = int(position[1]) 
# map[horizontal - 1][vertical -1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

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
users = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for for Scissors. \n"))
computer = random.randint(0,2)
computers_choice = options[computer]
if users >= 3 or users < 0:
    print("You typed an invalid number, you lose!")
else:
    users_choice = options[users]
    print(f"{computers_choice} \nComputer choice")
    print(f"{users_choice}")

    if users == computer:
        print("Draw")
    elif users == 0 and computer == 2:
        print("You win")
    elif users == 2 and computer == 1:
        print("You win")
    elif users == 1 and computer == 0:
        print("You win")
    else:
        print("You lose")

