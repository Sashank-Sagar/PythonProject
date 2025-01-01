import tkinter as tk
from tkinter import filedialog, messagebox

#Creating a new file function
def new_file():
    text.delete(1.0, tk.END)

#Opening a file function
def open_file():
    file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

#Saving a file function
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo('Info', 'File saved successfully!')

#Creating the main(root) window
root = tk.Tk()
root.title('My Notepad')
root.geometry('800x600')

#Creating the menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

#Creating the text widget
text = tk.Text(root, wrap=tk.WORD, font=('Arial', 14),fg='black',)
text.pack(expand=tk.YES, fill='both')

#Running the main loop
root.mainloop()