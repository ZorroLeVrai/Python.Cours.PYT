import tkinter as tk
from tkinter import messagebox

WIDTH = 800
HIGHT = 500
TITLE = "Ma première fenêtre"

root = tk.Tk()
root.geometry(f"{WIDTH}x{HIGHT}")
root.title(TITLE)

def on_closing():
    root.destroy()

def show_message():
    messagebox.showinfo(title="Message", message="Message à afficher")

#Add menus
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=on_closing)
filemenu.add_separator()
filemenu.add_command(label="Close Without Question", command=exit)

actionmenu = tk.Menu(menubar, tearoff=0)
actionmenu.add_command(label="Show Message", command=show_message)

menubar.add_cascade(menu=filemenu, label="File")
menubar.add_cascade(menu=actionmenu, label="Action")
root.config(menu=menubar)

root.mainloop()



