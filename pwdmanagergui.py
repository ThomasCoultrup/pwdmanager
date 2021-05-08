import tkinter as tk
from tkinter import filedialog, Text, StringVar
import os

#def clear_text_box():
  #clear any text in the text fields
  #text_box.delete(1.0, tk.END)
 # window.title("Password Manager")

def open_file():
  #open a file for editing
  filepath = filedialog.askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )

  if not filepath:
    return
  
  #clear_user_box()
  #clear_passwd_box()
  with open(filepath, "r") as input_file:
    text = input_file.read()
    user_box.insert(tk.END, text)

  window.title(f"Password Manager - {filepath}")


def save_file_as():
  #save the current file as a new file
  filepath = filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Text File", "*.txt")]
  )
  
  if not filepath:
    return
  
  with open(filepath, "a") as output_file:
    text1 = user_box.get()
    text2 = passwd_box.get()
    text3 = "\n"
    text4 = menu.get()
    output_file.write(text4)
    output_file.write(text3)
    output_file.write(text1)
    output_file.write(text3)
    output_file.write(text2)

  window.title(f"Password Manager - {filepath}")
   

window = tk.Tk()
window.title("Password Manager")
window.geometry("400x400")

button_frame = tk.Frame(master=window, width=50)
button_frame["relief"] = tk.GROOVE
button_frame["borderwidth"] = 2
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

greeting = tk.Label(text="Welcome to Password Manager")
greeting.pack()


frame1 = tk.Frame(master=window, width=100, height=100)
username = StringVar()
user_box = tk.Entry(window, textvariable=username)
user_box.pack()
userfield = "Username"
user_box.insert(tk.END, userfield)

def Entry1_Callback(event):
    user_box.selection_range(0, tk.END)
user_box.bind("<FocusIn>", Entry1_Callback)
user_box.focus() 

password = StringVar()
passwd_box = tk.Entry(window, textvariable=password, show="*")
passwd_box.pack()
pwdfield = "Password"
passwd_box.insert(tk.END, pwdfield)
frame1.pack()

menu = tk.StringVar()
menu.set("Select Platform")
drop_down = tk.OptionMenu(window, menu, "Reddit", "Porn Hub", "Netflix", "Disney Plus")
drop_down.pack()

open_button = tk.Button(master=button_frame)
open_button["text"] = "Open"
open_button.pack(fill=tk.X, padx=5, pady=5)

save_as_button = tk.Button(master=button_frame)
save_as_button["text"] = "Save As..."
save_as_button.pack(fill=tk.X, padx=5, pady=5)

#put clear button here


#clear_button["command"] = clear_text_box
open_button["command"] = open_file
save_as_button["command"] = save_file_as

window.mainloop()
