import tkinter as tk
from tkinter import font

HEIGHT = 550
WIDTH = 660

def add_list(action):
    with open('todo.txt', 'a') as f:
        content = f.write(action + "\n")
    read_todolist()

def read_todolist():
    f = open("todo.txt", "r", encoding="UTF8").read()
    label['text'] = f # change text in label

def verify_entry(entry):
    if entry and entry != " ":
        add_list(entry)
    else:
        print("ERROR: The new action can't be nothing or just a space ")


root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.ppm")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

entry = tk.Entry(root)
entry.place(relx = 0.05, rely = 0.05,relwidth = 0.5, relheight = 0.1)

button = tk.Button(root, text="Add", font=("Futura", 18), command= lambda: verify_entry(entry.get()))
button.place(relx = 0.60, rely = 0.05, relwidth = 0.3, relheight = 0.1)


label = tk.Label(root, font=("Futura", 26))
label.place(relx = 0.05, rely = 0.2, relwidth = 0.85, relheight = 0.75)

read_todolist()
root.mainloop()
