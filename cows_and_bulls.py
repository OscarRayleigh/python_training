# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number.
# Ask the user to user_digits a 4-digit number.
# For every digit that the user guessed correctly in the
# correct place, they have a “cow”. For every digit the
# user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a user_digits, tell them how
# many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the
# number of guesses the user makes throughout the game and
# tell the user at the end.
import random

def verify_entry():
    user_digits = input("Just write a 4 digits number \n")
    if len(user_digits) != 4:
        print("We need EXACTLY 4 digits !")
        user_digits = verify_entry()
    if user_digits.isdigit() == False:
        print("I SAID DIGIT ! :\n")
        user_digits = verify_entry()
    return user_digits

def compare_digits(user_digits, solution):
    bulls = 0
    cows = 0
    for x in range(0,4):
        if user_digits[x] == solution[x]:
            cows += 1
        elif user_digits[x] in solution:
            bulls += 1
    print("Bulls = ", bulls)
    print("Cows = ", cows)

def cows_and_bulls():
    user_digits = verify_entry()
    solution = "5641"#format(random.randint(0000,9999), '04d')
    print("Solution = ", solution)
    print("Entry = ", user_digits)
    compare_digits(user_digits, solution)
cows_and_bulls()
