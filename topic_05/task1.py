import random

options = ["stone", "scissor", "paper"]
user_choice = input("Enter your choice (stone, scissor, paper): ")
computer_choice = random.choice(options)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("Draw")
elif user_choice == "stone" and computer_choice == "scissor":
    print("You win")
elif user_choice == "scissor" and computer_choice == "paper":
    print("You win")
elif user_choice == "paper" and computer_choice == "stone":
    print("You win")
else:
    print("Computer wins")
