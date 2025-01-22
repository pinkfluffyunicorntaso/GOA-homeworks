from turtle import *


#paint a house
speed(30)
width(7)
color("pink")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)

#door
color("blue")

begin_fill()
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
#roof
color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60,120)
pendown()

#window

color("gray")
right(60)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
right(180)
forward(22.5)
right(90)
forward(45)

penup()
goto(35.6,120)
pendown()
left(90)
forward(45)

penup()
goto(140,120)
pendown()

left(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
left(180)
forward(22.5)
left(90)
forward(45)

penup()
goto(162.5,120)
pendown()
right(90)
forward(45)

exitonclick()