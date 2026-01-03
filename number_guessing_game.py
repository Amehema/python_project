import random

randno=random.randint(1,100)
try:
    while True:
        guess=int(input("Guess the number:"))
        if randno > guess:
            print("number is too low..")
        elif randno < guess:
            print("number is too higher..")
        else:
            print("Congratulation! your guess is correct :)")
            break
except ValueError:
    print("Please enter a valid number..")