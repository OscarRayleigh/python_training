import os

user_input = int(input("Enter a number : "))

liste = list(range(2, user_input + 1))

for i in liste:
    for element_liste in liste:
        if element_liste % i == 0 and element_liste != i:
            liste.remove(element_liste)

for i in liste:
    print(i)

os.system("pause")
