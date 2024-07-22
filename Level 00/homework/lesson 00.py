from turtle import *


#square 
speed(30)

width(7)
color("purple")


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#window
penup()
goto(30,150)
pendown()
left(120)
color("blue")
begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()
#window2
penup()
goto(170,150)
pendown()
color("blue")
begin_fill()
right(90)
forward(20)

right(90)
forward(20)

right(90)
forward(20)

right(90)
forward(20)
end_fill()






exitonclick()