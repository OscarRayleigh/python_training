import random

def find_random_word():
    f = open("words.txt", "r")
    all = f.readlines()
    x = random.randrange(1371)
    f.close()
    return all[x].upper()

word = find_random_word()
letters_left = "_"*(len(word)-1)
letters_found = []
letters_not_in_list = []
attempts = 7

def update_hangman(user_input, word):
    global letters_left
    global letters_found
    global letters_not_in_list
    indexes = [index for index, value in enumerate(list(word)) if value == user_input]
    print(type(indexes))
    letters_left = list(letters_left)
    for index in indexes:
        letters_left[index] = user_input
    if user_input not in letters_found:
        letters_found.append(user_input)
    status()
    win_check(letters_left)

def main():
    is_part_of_word(word)

def take_input_and_verify():
    rules_ok = False
    while not rules_ok:
        user_input = input("Try to guess the word ! : ").upper()
        if user_input.isalpha() and len(user_input) == 1:
            rules_ok = True
            return user_input

        if len(user_input) > 1 :
            print("Only one char at a time\n")
            status()
        if not user_input.isalpha():
            print("Only letters from alphabet !")
            status()

def is_part_of_word(word):
    global attempts
    status()
    win = False
    while not win:
        user_input = take_input_and_verify()
        print(user_input)
        if user_input in word:
            update_hangman(user_input, word)
        elif not user_input in word:
            attempts -= 1
            if user_input not in letters_not_in_list:
                letters_not_in_list.append(user_input)
            if attempts <= 0:
                print("You lost !\nThe word was", word)
                exit()
            status()

def win_check(letters_left):
    if not "_" in letters_left:
        print("You won !")
        exit()

def status():
    print("------------------------------------------------------------------------------------------")
    print("WORD : ", " ".join(letters_left))
    print("\nLetters found : ", " : ".join(letters_found))
    print("Letters that are not part of the word : ", " : ".join(letters_not_in_list))
    hangman_stat(attempts)
    print("Attempts left : {}".format(attempts))

def hangman_stat(attempts):
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    print(HANGMANPICS[attempts-1])

main()
