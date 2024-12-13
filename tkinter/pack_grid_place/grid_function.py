import tkinter as tk

WIDTH = 800
HIGHT = 500
TITLE = "Ma fenêtre"
font_style = ("Arial", 16)

root = tk.Tk()
root.geometry(f"{WIDTH}x{HIGHT}")
root.title(TITLE)

windowframe = tk.Frame(root)
#configure 2 columns
windowframe.columnconfigure(0, weight=1)
windowframe.columnconfigure(1, weight=1)

label = tk.Label(windowframe, text="Bonjour", font=font_style)
label.grid(row=0, column=0, sticky="nsew")

# An entry is a textbox with a height of 1 (1 line)
myentry = tk.Entry(windowframe)
myentry.grid(row=0, column=1, sticky="nsew")

#Button widget
button1 = tk.Button(windowframe, text="One", font=font_style)
button1.grid(row=1, column=0, sticky="nsew")

button2 = tk.Button(windowframe, text="Two", font=font_style)
button2.grid(row=1, column=1, sticky="nsew")

windowframe.pack(anchor="w")
root.mainloop()
