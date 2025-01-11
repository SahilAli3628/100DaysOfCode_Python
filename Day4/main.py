import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to the game of Rock Paper Scissors!\nTime for your selection\n1.Rock\n2.Paper\n3.Scissors")
choice = input("What do you choose? (1/2/3): ")
options = ["Rock", "Paper", "Scissors"]

if choice == '1':
    choice = options[0]
    print(Rock)
elif choice == '2':
    choice = options[1]
    print(Paper)
elif choice == '3':
    choice = options[2]
    print(Scissors)
else:
    print("Enter a valid option next time!!!")
    exit()

comp_choice = random.choice(options)
print(f"The Computer chose {comp_choice}")
if comp_choice == "Rock":
    print(Rock)
if comp_choice == "Paper":
    print(Paper)
if comp_choice == "Scissors":
    print(Scissors)

if choice == "Rock" and comp_choice == "Paper":
    print("You Lose!!!")
elif choice == "Rock" and comp_choice == "Scissors":
    print("You Win!!!")
elif choice == "Paper" and comp_choice == "Scissors":
    print("You Lose!!!")
elif choice == "Paper" and comp_choice == "Rock":
    print("You Win!!!")
elif choice == "Scissors" and comp_choice == "Rock":
    print("You Lose!!!")
elif choice == "Scissors" and comp_choice == "Paper":
    print("You Win!!!")
elif choice == comp_choice:
    print("Draw!!! You both chose the same")
