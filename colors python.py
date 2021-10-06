#Initialization
import turtle
import random
shea=turtle.Turtle()
shea.left(90)
turtle.colormode(255)
shea.speed(22)
import random
#Function
def randomDot():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    c = random.randint(0,200)
    shea.color(r,b,g)
    shea.begin_fill()
    shea.circle(c)
    shea.end_fill()
    

#Main
for i in range(100):
    x=random.randint(100,235)
    y=random.randint(100,235)
    shea.penup()
    shea.goto(x,y)
    shea.pendown()
    randomDot()

