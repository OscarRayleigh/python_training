from random import randrange

def guess_the_number():
    didntguess = True
    n = input("Let's choose n :")
    while not (n.isdigit()):
        n = input("Something wrong happened! Gimme n ! :")
    tries = 1
    sol = randrange(int(n))
    while didntguess:
        user_input = input("Guess the number ! :")
        while not (user_input.isdigit()):
            user_input = input("Something wrong happened! Guess the number ! :")
        if sol > int(user_input):
            print("Nah its higher !")
            tries+=1
        if sol < int(user_input):
            print("its actually lower ...")
            tries+=1
        elif sol == int(user_input) :
            didntguess = True
            if tries <= 2*int(int(n)**(1/3)):
                print("You guessed right in %d times !! GG ! or not ... ? idk i'm just a program lmao" % (tries))
            else:
                print("You guessed right in ... %d times ... You didnt win but you don't have to be ashamed" % (tries))
                didntguess = True
            replay = input("Do you wanna play again ? y for yes and n for no : ")
            if replay.lower() == 'y' or replay.lower() == "yes":
                guess_the_number()
            if replay.lower() == 'n' or replay.lower() == "no":
                print("Well it was good playing with you m8 ! see ya !! \n")
            else:
                print("I guess I didnt understand what you wrote, program's closing ! \n")
            break

print(" Hi ! And welcome to my game ! You'll have guess a number between 0 and n and you choose n, you actually choose the difficulty ! \n")
print("n = 100 : You're a beginner\n")
print("n = 1000 : Still quite easy lmao\n")
print("n = 10000 : Alright men you have nothing to prove ...\n")
print("n = 100000 : looks like you have time to loose \n")

guess_the_number()
