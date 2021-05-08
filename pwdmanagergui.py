import tkinter as tk
from tkinter import filedialog, Text, StringVar
import os
from define_buttons import clear_results_box, open_file, save_file_as



window = tk.Tk()
window.title("Password Manager")
window.geometry("400x400")

button_frame = tk.Frame(master=window, width=50)
button_frame["relief"] = tk.GROOVE
button_frame["borderwidth"] = 2
button_frame.pack(side=tk.BOTTOM, fill=tk.X)


greeting = tk.Label(text="Welcome to Password Manager")
greeting.pack()


frame1 = tk.Frame(master=window, width=50, height=50)
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

results_return = StringVar()
results_box = tk.Text(window)
results_box.place(x = 107, y = 150, height = 100, width = 186)
resultsfield = ""
results_box.insert(tk.END, resultsfield)


menu = tk.StringVar()
menu.set("Select Platform")
drop_down = tk.OptionMenu(window, menu, "Reddit", "Porn Hub", "Netflix", "Disney Plus")
drop_down.pack()
frame1.pack()


open_button = tk.Button(master=button_frame)
open_button["text"] = "Open"
open_button.pack(fill=tk.X, padx=5, pady=5)

save_as_button = tk.Button(master=button_frame)
save_as_button["text"] = "Save As..."
save_as_button.pack(fill=tk.X, padx=5, pady=5)


clear_button = tk.Button(master=button_frame)
clear_button["text"] = "Clear"
clear_button.pack(fill=tk.X, padx=5, pady=5)


clear_button["command"] = clear_results_box
open_button["command"] = open_file
save_as_button["command"] = save_file_as

window.mainloop()
