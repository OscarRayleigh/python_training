# Write a Python program to create //
# all possible strings by using a few char

import random
import math
from collections import Counter
import os
user_data = input("Just smash your keyboard !\n")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()


x = 0
final_output = 0
cool_list = []
unic_char_list = []
rep_char = {}
foo = {}
i = 0
char_list = []
char_list[:] = user_data
maximum = math.factorial(len(char_list))
rep = dict(Counter(char_list))

print("--------------------------- Total of repetitions --------------------------- ")

while x < len(char_list):
    print("Occurence of", char_list[x], "is %s" % rep.get(char_list[x]))
    if char_list[x] not in unic_char_list:
        rep.get(char_list[x])
        unic_char_list.append(char_list[x])
        if rep.get(char_list[x]) > 1:
            rep_char = {char_list[x]: rep.get(char_list[x])}
            foo.update(rep_char)
    x += 1
print("Unique char : ", unic_char_list)
print("Characters repeated more than once following the synthax char:occurence = ", foo)
for k in foo.keys():
    maximum //= math.factorial(foo[k])
print("Combinaisons with the given characters =  ", maximum)



while i < maximum:
    words = ""
    random.shuffle(char_list)
    words = ''.join(char_list)
    if words in cool_list:
        continue
    if words not in cool_list:
        cool_list.append(words)
        print(cool_list[final_output])
        i += 1
    final_output += 1 

