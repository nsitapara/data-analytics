# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == "r" and user_choice == "p":
    print("You Win")
elif computer_choice =="p" and user_choice == "s":
    print("you Win")
elif computer_choice =="s" and user_choice == "r":
    print("you Win")
elif computer_choice == user_choice:
    print("Draw")
else:
    print("You Lose")


print("You Picked: ", user_choice, "Computer Picked: ", computer_choice)