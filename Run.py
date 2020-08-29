from tkinter import*
from tkinter import filedialog
import os
import re

current_path = os.getcwd()
program_path = current_path + "/Program"
python_path = program_path + "/Python"

root= Tk()
root.geometry("1600x800+0+0")
root.title("Epicness Generator")

Tops = Frame(root, width = 1600,height = 50)
Tops.pack(side=TOP)

f0 = Frame(root, width = 800,height = 200, relief=SUNKEN)
f0.pack(side=TOP)
f1 = Frame(root, width = 800,height = 500, relief=SUNKEN)
f1.pack(side=TOP)

lblInfo = Label(Tops, font=('arial',25,'bold'),text="Welcome to the Python programs execution section.\n",fg="Dark Blue", bd=5, anchor='w')
lblInfo.grid(row=0,column=0)

root.filename =  filedialog.askopenfilename(initialdir = python_path,title = "Select file",filetypes = (("Python files","*.py"),("all files","*.*")))
file_name = (root.filename)
parts = file_name.split("/")
file_name = parts[-1]
parts = file_name.split(".")
file_name = parts[0]
#file_name = input("Enter the name of the file you want to resume working on.\n")
file_path = python_path + "/" + file_name + ".py"
root.destroy()

file = open(file_path,"r")
file_content = file.read()
file.close()

exec(file_content)
