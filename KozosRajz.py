import turtle

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
turtle.done()