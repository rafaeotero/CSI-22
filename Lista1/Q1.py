import turtle
def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() 
wn.bgcolor("lightgreen")
alex = turtle.Turtle() 
for n in range (5):
    alex.penup()
    alex.goto(-10*n,-10*n)
    alex.pendown()
    draw_square(alex, 20*(n+1))
wn.mainloop()

