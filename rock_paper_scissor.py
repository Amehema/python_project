import random

Rock='r'
Paper='p'
Scissor='s'
emojis={Rock:'🥌',Paper:'📜',Scissor:'✂'}
choices=tuple(emojis.keys())

def get_user_choice():
     while True:
        user_choices=input("Rock paper or scissor(r/p/s): ").lower()
        if user_choices in choices:
            return user_choices
        else:
            print('Invalid choice :(')

def display_choices(user_choice,computer_choice):
    print(f"Your choice {emojis[user_choice]}")
    print(f"Computer choice {emojis[computer_choice]}")
 
def determine_choice(user_choice,computer_choice):
    if user_choice == computer_choice:
        print('tie...')
    elif (
        (user_choice==Rock and computer_choice==Paper) or 
        (user_choice==Paper and computer_choice==Scissor) or 
        (user_choice==Scissor and computer_choice==Rock)):
        print("You lose :(")
    else:
        print("You win :)")
        
def play_game():
    while True:
        user_choice=get_user_choice()
        computer_choice=random.choice(choices)

        display_choices(user_choice,computer_choice)

        determine_choice(user_choice,computer_choice)

        user_continue=input("Continue? (y/n): ").lower()
        if user_continue=='n':
            print("bye")
            break

play_game()
