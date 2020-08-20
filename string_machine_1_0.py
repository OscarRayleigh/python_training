# Write a Python program to create //
# all possible strings by using a few char
# this code doesnt work
import random
import math
from collections import Counter


char_list = ['a', 'e', 'y', 'o']
cool_list = []
final_output = 0

x = 0
rep = dict(Counter(char_list))
print("Total of occurences : ")
unic_char_list = []
rep_char = {}
foo = {}
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
print("Char repeated more than once following the synthax char:occurence = ", foo)
maximum = math.factorial(len(char_list))
for k in foo.keys():
    maximum //= math.factorial(foo[k])

print("maximum =  ", maximum)
i = 0
while i < maximum:
    words = ""
    random.shuffle(char_list)
    words = ''.join(char_list)
    if words in cool_list:
        continue
    if words not in cool_list:
        cool_list.append(words)
        #final_output -= 1
        print(cool_list[final_output])
        i += 1
    final_output += 1
    print(i)
print(maximum)
