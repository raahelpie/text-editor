from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import ImageTk, Image


def new_file():
    text.delete(0.0, END)


def open_file():
    file1 = askopenfile(mode='r')
    data = file1.read
    text.delete(0.0, END)
    text.insert(0.0, data)


def save_file():
    filename = "Untitled.txt"
    data = text.get(0.0, END)
    file1 = open(filename, 'w')
    file1.write(data)


def save_as():
    file1 = asksaveasfile(mode='w')
    data = text.get(0.0, END)
    file1.write(data)


gui = Tk()
gui.title("Text Editor")
gui.geometry("600x500")
text = Text(gui, font="Bahnschrift")
text.pack()


mymenu = Menu()
list1 = Menu()
list1.add_command(label="New File", command=new_file)
list1.add_command(label="Open File", command=open_file)
list1.add_command(label="Save", command=save_file)
list1.add_command(label="Save As", command=save_as)
list1.add_command(label="Exit", command=gui.quit)
mymenu.add_cascade(label="File", menu=list1)
gui.config(menu=mymenu)


gui.mainloop()

