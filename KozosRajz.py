import turtle

turtle.bgcolor("light blue")
hossz=50

turtle.fillcolor("grey")
turtle.begin_fill()
i=0
while i<2:
    turtle.forward(hossz)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    i+=1
turtle.end_fill()

turtle.forward(-hossz)

turtle.fillcolor("black")
turtle.begin_fill()

z=0
while z<2:
    turtle.forward(3*hossz)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    z+=1
turtle.end_fill()

turtle.forward(75)

k = 0
while k < 3:
    if k == 0:
        turtle.fillcolor("green")
    elif k == 1:
        turtle.fillcolor("yellow")
    else:
        turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(35)
    turtle.penup()
    turtle.left(90)
    turtle.forward(70+25)
    turtle.right(90)
    turtle.pendown()
    turtle.end_fill()

    k +=1

turtle.done()