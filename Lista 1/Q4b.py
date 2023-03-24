import turtle
def draw_Spiral(t, n, sz, increase):
    for i in range(n):
        t.forward(sz+i*increase)
        t.left(89)

wn = turtle.Screen() 
wn.bgcolor("lightgreen")
alex = turtle.Turtle() 
draw_Spiral(alex, 100, 2, 2)
wn.mainloop()