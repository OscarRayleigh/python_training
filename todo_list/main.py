import tkinter as tk
from tkinter import font
import os.path

HEIGHT = 550
WIDTH = 660



if os.path.isfile('./todo.txt') == False:
    f = open("todo.txt", "x")
    print("Creating todo.txt")

def read_todolist():
    #my_todolist = []
    #with open('todo.txt', 'r') as f:
        # for line in f:
        #     my_todolist.append(line)
        #
        # if len(my_todolist) > x:
        #     return my_todolist[x]
        # else:
        #     return ""
        f = open("todo.txt", "r", encoding="UTF8").read()
        label['text'] = f


def add_list(action):
    with open('todo.txt', 'a') as f:
        content = f.write(action + "\n")
    read_todolist()

# def read_todolist():
#     f = open("todo.txt", "r", encoding="UTF8").read()
#     label['text'] = f # change text in label

def verify(entry):
    lines = len(open("todo.txt").readlines(  ))
    if lines >= 11:
        print("More than eleven action already in the list")
    if lines < 11:
        if entry and entry != " " and len(entry) <= 40:
            add_list(entry)
        else:
            print("ERROR: The new action is either too long, empty or just a space ")


root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.ppm")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

entry = tk.Entry(root)
entry.place(relx = 0.05, rely = 0.05,relwidth = 0.5, relheight = 0.1)

#Bruteforcing the button creation, I could use OOP I know
button = tk.Button(root, text="Add", font=("Futura", 18), command= lambda: verify(entry.get()))
button.place(relx = 0.60, rely = 0.05, relwidth = 0.3, relheight = 0.1)

label = tk.Label(root, font=("Futura", 26), anchor="nw")
label.place(relx = 0.05, rely = 0.2, relwidth = 0.70, relheight = 0.77)

del_1 = tk.Button(root, text="Done", font=("Futura", 18))
del_1.place(relx = 0.75, rely = 0.2, relwidth = 0.2, relheight = 0.07)

del_2 = tk.Button(root, text="Done", font=("Futura", 18))
del_2.place(relx = 0.75, rely = 0.27, relwidth = 0.2, relheight = 0.07)

del_3 = tk.Button(root, text="Done", font=("Futura", 18))
del_3.place(relx = 0.75, rely = 0.34, relwidth = 0.2, relheight = 0.07)

del_4 = tk.Button(root, text="Done", font=("Futura", 18))
del_4.place(relx = 0.75, rely = 0.41, relwidth = 0.2, relheight = 0.07)

del_5 = tk.Button(root, text="Done", font=("Futura", 18))
del_5.place(relx = 0.75, rely = 0.48, relwidth = 0.2, relheight = 0.07)

del_6 = tk.Button(root, text="Done", font=("Futura", 18))
del_6.place(relx = 0.75, rely = 0.55, relwidth = 0.2, relheight = 0.07)

del_7 = tk.Button(root, text="Done", font=("Futura", 18))
del_7.place(relx = 0.75, rely = 0.62, relwidth = 0.2, relheight = 0.07)

del_8 = tk.Button(root, text="Done", font=("Futura", 18))
del_8.place(relx = 0.75, rely = 0.69, relwidth = 0.2, relheight = 0.07)

del_9 = tk.Button(root, text="Done", font=("Futura", 18))
del_9.place(relx = 0.75, rely = 0.76, relwidth = 0.2, relheight = 0.07)

del_10 = tk.Button(root, text="Done", font=("Futura", 18))
del_10.place(relx = 0.75, rely = 0.83, relwidth = 0.2, relheight = 0.07)

del_11= tk.Button(root, text="Done", font=("Futura", 18))
del_11.place(relx = 0.75, rely = 0.90, relwidth = 0.2, relheight = 0.07)


read_todolist()
root.mainloop()
