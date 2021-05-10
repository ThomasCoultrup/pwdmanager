import tkinter as tk
from tkinter import filedialog, Text, StringVar
import os


def clear_results_box():
  #clear any text in the text fields
  results_box.delete(1.0, tk.END)
  window.title("Password Manager")

def open_file():
  #open a file for editing
  filepath = filedialog.askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )

  if not filepath:
    return
  
  clear_results_box()
  with open(filepath, "r") as input_file:
    text = input_file.read()
    results_box.insert(tk.END, text)

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
    text4 = platform_box.get()
    text5 = "User: "
    text6 = "Pass: "
    text7 = "Plat: "
    output_file.write(text7)
    output_file.write(text4)
    output_file.write(text3)
    output_file.write(text5)
    output_file.write(text1)
    output_file.write(text3)
    output_file.write(text6)
    output_file.write(text2)

  window.title(f"Password Manager - {filepath}")

window = tk.Tk()
window.title("Password Manager")
window.geometry("400x400")

frame1 = tk.Frame(master=window, width=50, height=50)
frame1.pack()

button_frame = tk.Frame(master=window, width=50)
button_frame["relief"] = tk.GROOVE
button_frame["borderwidth"] = 2
button_frame.pack(side=tk.BOTTOM, fill=tk.X)


user_box_label = tk.Label(master=frame1)
user_box_label["text"] = "Username:"
user_box_label.grid(row=0, column=0)

passwd_box_label = tk.Label(master=frame1)
passwd_box_label["text"] = "Password:"
passwd_box_label.grid(row=1, column=0)

platform_box_label = tk.Label(master=frame1)
platform_box_label["text"] = "Platform:"
platform_box_label.grid(row=2, column=0)


username = StringVar()
user_box = tk.Entry(master=frame1, textvariable=username)
user_box.grid(row=0, column=1)


def Entry1_Callback(event):
    user_box.selection_range(0, tk.END)
user_box.bind("<FocusIn>", Entry1_Callback)
user_box.focus() 

password = StringVar()
passwd_box = tk.Entry(master=frame1, textvariable=password, show="*")
passwd_box.grid(row=1, column=1)

platform = StringVar()
platform_box = tk.Entry(master=frame1, textvariable=platform)
platform_box.grid(row=2, column=1)

results_return = StringVar()
results_box = tk.Text(master=window)
results_box.place(x = 107, y = 150, height = 100, width = 186)
resultsfield = ""
results_box.insert(tk.END, resultsfield)


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
