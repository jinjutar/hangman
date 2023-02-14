import time
import random

name = input("What is your name?")
print("Hello "+name+" ,let's start playing hangman")
time.sleep(2)
print("Start guessing......\n")
time.sleep(1)

secretWords = ['salmon', 'tuna', 'sushi', 'taco', 'noodle']
word = random.choice(secretWords)

guesses = ''
turns = 6

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")

        else:
            failed += 1
            print("_", end="")

    if failed == 0:
        print("\nyou won")
        break

    guess = input("\n guess character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nwrong")
        print("\nyou have " + str(turns) + " more guess")
        if turns == 0:
            print("\nyou lost")












