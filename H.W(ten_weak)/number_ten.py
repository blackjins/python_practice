import turtle 
wn = turtle.Screen()
top = turtle.Turtle()
mid = turtle.Turtle()
bot = turtle.Turtle()
def draw_top(x, y):    
    top.pu()
    top.goto(x, y)
    top.pd()
    for i in range(0, 2):
        top.fd(200)
        top.rt(90)
        top.fd(20)
        top.rt(90)
def draw_mid(x, y):    
    top.pu()
    top.goto(x, y)
    top.pd()
    for i in range(0, 2):
        top.fd(150)
        top.rt(90)
        top.fd(20)
        top.rt(90)
def draw_bot(x, y):    
    top.pu()
    top.goto(x, y)
    top.pd()
    for i in range(0, 2):
        top.fd(100)
        top.rt(90)
        top.fd(20)
        top.rt(90)
draw_top(-480, -240)
draw_mid(-480, -200)
draw_bot(-480, -160)


wn.exitonclick()