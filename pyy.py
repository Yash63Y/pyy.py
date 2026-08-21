import turtle

screen = turtle.Screen()
screen.bgcolor("black")

spiral = turtle.Turtle()
spiral.speed(0)
colors = ["red","purple","blue","green","orange","yellow"]

for x in range(360):
    spiral.pencolor(colors[x % 6])
    spiral.width(x//100+1)
    spiral.forward(x)
    spiral.left(59)
    
turtle.update()
turtle.done()
    