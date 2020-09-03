# Write a Python program to create //
# all possible strings by using 'a', 'e', 'i', 'o', 'u'.
# Use the characters exactly once.

import random
import math
import os
from collections import Counter

user_data = input("smash\n")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
char_list = []
char_list[:] = user_data
cool_list = []
maximum = math.factorial(len(char_list))
x = 0
rep = dict(Counter(char_list))
unic_char_list = []
rep_char = {}
foo = {}

while x < len(char_list):
    if char_list[x] not in unic_char_list:
        rep.get(char_list[x])
        unic_char_list.append(char_list[x])
        if rep.get(char_list[x]) > 1:
            rep_char = {char_list[x]: rep.get(char_list[x])}
            foo.update(rep_char)
    x += 1

for k in foo.keys():
    maximum //= math.factorial(foo[k])

i = 0
final_output = 0
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
