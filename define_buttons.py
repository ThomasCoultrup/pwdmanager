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
    text4 = menu.get()
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