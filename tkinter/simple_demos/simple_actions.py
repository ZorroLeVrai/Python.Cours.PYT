import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        #Subscribe to the window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        #get the value from the textbox from beginning to end
        textbox_value = self.textbox.get('1.0', tk.END)
        messagebox.showinfo(title="Message", message=textbox_value)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit ?"):
            #Close the Window
            self.root.destroy()

MyGUI()
