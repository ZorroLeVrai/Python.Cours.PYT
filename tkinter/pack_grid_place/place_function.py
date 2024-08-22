import tkinter as tk

WIDTH = 800
HIGHT = 500
TITLE = "Ma fenêtre"
font_style = ("Arial", 16)

root = tk.Tk()
root.geometry(f"{WIDTH}x{HIGHT}")
root.title(TITLE)

label = tk.Label(root, text="Bonjour", font=font_style)
label.place(x=0, y=0, height=50, width=100)

# An entry is a textbox with a height of 1 (1 line)
myentry = tk.Entry(root)
myentry.place(x=100, y=0, height=50, width=100)

#Button widget
button1 = tk.Button(root, text="One", font=font_style)
button1.place(x=0, y=50, height=50, width=100)

button2 = tk.Button(root, text="Two", font=font_style)
button2.place(x=100, y=50, height=50, width=100)

root.mainloop()
