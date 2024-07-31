import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        #Add Widgets
        self.label = tk.Label(self.root, text="Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        #bind a specific action to a function
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        #Add menus
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        self.root.config(menu=self.menubar)

        #Subscribe to the window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def clear(self):
        self.textbox.delete("1.0", tk.END)

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()

    def show_message(self):
        textbox_value = self.textbox.get('1.0', tk.END)
        messagebox.showinfo(title="Message", message=textbox_value)


    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit ?"):
            #Close the Window
            self.root.destroy()

MyGUI()
