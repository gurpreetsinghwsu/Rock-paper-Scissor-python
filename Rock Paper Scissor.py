import random
user_actions = input("Enter what you want: (rock,paper,scissors) ") #from where user will select
possible_actions = ["rock", "paper", "scissors" ] #fixing values in tuple
computer_actions = random.choice(possible_actions) #letting computer take random value from turplex
print(f"\nYou chose {user_actions}, computer chose {computer_actions}.\n")

if user_actions == computer_actions:
    print(f"Both players selected{user_actions}, It's a tie")
elif user_actions == "rock":
    if user_actions == "scissors":
        print("User win")
    else:
        print("User lose")
elif user_actions == "paper":
    if computer_actions == "rock":
        print("User win")
    else:
        print("User lose")
elif user_actions == "Scissors":
    if computer_actions == "paper":
        print("User win")
    else:
        print("User lose")

