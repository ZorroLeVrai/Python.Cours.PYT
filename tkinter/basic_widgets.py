import tkinter as tk

WIDTH = 800
HIGHT = 500
TITLE = "Ma première fenêtre"

#Window
root = tk.Tk()
root.geometry(f"{WIDTH}x{HIGHT}")
root.title(TITLE)

#Label widget
label = tk.Label(root, text="Bonjour", font=("Arial", 18))
label.pack(padx=20, pady=20)

#Text widget
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10)

# An entry is a textbox with a height of 1 (1 line)
myentry = tk.Entry(root)
myentry.pack(pady=10)

#Button widget
button = tk.Button(root, text="Click Me!", font=("Arial", 18))
button.pack(padx=10, pady=10)

root.mainloop()
