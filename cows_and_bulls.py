# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the
# correct place, they have a “cow”. For every digit the
# user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how
# many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the
# number of guesses the user makes throughout the game and
# tell the user at the end.
import random

def cows_and_bulls():
    str = input("Juste write a 4 digits number : \n")
    if len(str) != 4:
        print("We need EXACTLY 4 digits !")
        cows_and_bulls()
    if str.isdigit() == False:
        print("I SAID DIGIT ! :\n")
        cows_and_bulls()
    solution = format(random.randint(0000,9999), '04d')
    print(solution)

#todo write a checker function



cows_and_bulls()
