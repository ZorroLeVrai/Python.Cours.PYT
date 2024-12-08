import turtle as tl

def draw_spiral(t: tl.Turtle, angle: float, nb_interations: int):
    colors = ["red", "dark red"]
    for number in range(nb_interations):
        t.pencolor(colors[number % 2])
        t.forward(number + 1)
        t.right(angle)

def draw_square(t: tl.Turtle, size: int):
    for _ in range(4):
        t.forward(size)
        t.right(90)

tl.speed(1000)
tl.bgcolor("black")
t = tl.Turtle()
t.pencolor("white")
#draw_spiral(t, 89, 100)
draw_square(t, 100)

#t.screen.mainloop()
tl.done()