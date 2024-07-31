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

buttonframe = tk.Frame(root)
#configure 3 columns
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#Button widget
button_font = ("Arial", 18)
btn1 = tk.Button(buttonframe, text="1", font=button_font)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=button_font)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=button_font)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=button_font)
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=button_font)
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=button_font)
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

another_button = tk.Button(root, text="Placed Button")
another_button.place(x=200, y=300, height=100, width=100)

root.mainloop()
