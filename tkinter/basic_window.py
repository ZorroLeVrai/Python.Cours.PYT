import tkinter as tk

WIDTH = 800
HIGHT = 500
TITLE = "Ma première fenêtre"

root = tk.Tk()
root.geometry(f"{WIDTH}x{HIGHT}")
root.title(TITLE)

root.mainloop()
