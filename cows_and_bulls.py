# Create a program that will play the “bulls and cows” game with the user. The game works like this:
# Randomly generate a 4-digit number.
# Ask the user to user_digits a 4-digit number.
# For every digit that the user guessed correctly in the
# correct place, they have a “cow”. For every digit the
# user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a user_digits, tell them how
# many “bulls” and “cows” they have. Once the user guesses
# the correct number, the game is over. Keep track of the
# number of guesses the user makes throughout the game and
# tell the user at the end.
import random

solution = []
tries = 0

def making_sol(solution):
    for i in range(4):
        x = random.randint(0,9)
        solution.append(x)
    if len(solution) > len(set(solution)):
        solution.clear()
        solution = making_sol(solution)
    return(solution)

def bulls_and_cows():
    global tries
    cows = 0
    bulls = 0
    guess = []
    print(solution)
    user_digits = input("Just write a 4 digits number with no repetitions : ")
    if len(user_digits) != 4:
        print("You should write exacly 4 digits !")
        bulls_and_cows()

    for char in user_digits:
      count = user_digits.count(char)
      if count > 1:
          print("\n You just wrote a digit more than once ! \n")
          bulls_and_cows()
    tries += 1
    for i in range(4):
        guess.append(int(user_digits[i]))
    for i in range(4):
        for j in range(4):
            if (guess[i] == solution[j] and i != j):
                bulls += 1

    for x in range(4):
        if (guess[x] == solution[x]):
            cows +=1
    print("cows = ", cows)
    print("bulls = ", bulls)
    if(cows == 4):
        print("You just won in %d tries !" % (tries))
        play_again = input("Do you wanna play again ? Press y to play again :")
        if play_again == 'y':
            making_sol(solution)
            bulls_and_cows()
    if(cows != 4):
        bulls_and_cows()
making_sol(solution)
bulls_and_cows()
