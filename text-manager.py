# w - write. if file does not exist,
# python create this file
#with open("file.txt", "w") as file:
# file.write("Hello world!")

# a - append.
#with open("file.txt", "a") as file:
# file.write(" Hello user!")

#with open("file.txt", "r") as file:
# print(file.read())

import tkinter as tk
from tkinter import  filedialog

def save():
  text = text_box.get("1.0", tk.END)
  file_name = filedialog.asksaveasfilename(defaultextension=".txt")
  if file_name:
     with open(file_name, "w") as file:
        file.write(text)

def upload():
    file_name = filedialog.askopenfilename(defaultextension=".txt")
    if file_name:
        with open(file_name, "r") as file:
            text = file.read()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

def delete():
    text_box.delete("1.0", tk.END)

def append():
    text = text_box.get("1.0", tk.END)
    file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_name:
        with open(file_name, "a") as file:
            file.write(text)
# сделать кнопку очистки
# сделать кнопку добавление в файл а не вставки

root = tk.Tk()
root.title("editor")
text_box = tk.Text(root, width=60, height=20)
text_box.pack()

tk.Button(root, text="save", command=save).pack(side="left")
tk.Button(root, text="upload", command=upload).pack(side="left")

root.mainloop()
