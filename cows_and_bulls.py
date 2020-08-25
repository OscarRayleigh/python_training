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
solution = []
def making_sol():
    for i in range(4):
        x = random.randrange(0,9)
        solution.append(x)
    if len(solution) > len(set(solution)):
        solution.clear()
        making_sol()

def cows_and_bulls():
    bulls = 0
    cows = 0
    guess = []
    user_digits = input("Just write a 4 digits number \n")

    for i in range(4):
        guess.append(int(user_digits[i]))
    for i in range(4):
        for j in range(4):
            if guess[i] == solution[j]:
                cows += 1

    for x in range(4):
        if (guess[x] == solution[x]):
            bulls +=1
    print("Bulls = ", bulls)
    print("Cows = ", cows)
    print("Solution =", solution)
    if(bulls == 4):
        print("You won bro ! ")
    if(bulls != 4):
        cows_and_bulls()
# def old():
#     user_digits = verify_entry()
#     print("Solution = ", solution)
#     print("Entry = ", user_digits)
#     compare_digits(user_digits, solution)
making_sol()
cows_and_bulls()
