import re

def greater_than_x():
    print("ONLY INT ! --\n")
    x = input("Gimme the x :  ")
    user_data = input("smash ur numpad !  :  ")

    if re.search('[a-zA-Z]', user_data)or re.search('[a-zA-Z]', x):
        print("Incorrect entry ! ")
        greater_than_x()

    a = split(user_data)
    j=0

    for i in a:
        if int(a[j][0]) > int(x):
            print(a[j][0])
        j+=1
def split(user_data):
    return [char for char in user_data]

greater_than_x()
