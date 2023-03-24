import turtle
def draw_RecSpiral(t, n, sz, increase):
    for i in range(n):
        t.forward(sz+i*increase)
        t.left(90)

wn = turtle.Screen() 
wn.bgcolor("lightgreen")
alex = turtle.Turtle() 
draw_RecSpiral(alex, 100, 2, 2)
wn.mainloop()