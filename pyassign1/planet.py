"""

__author__ = "huangyang"

__pkuid__  = "1700011776"

__email__  = "1700011776@pku.edu.cn"

"""

import math

import turtle
<<<<<<< HEAD

a0=turtle.Turtle()

a1=turtle.Turtle()

a2=turtle.Turtle()

a3=turtle.Turtle()

a4=turtle.Turtle()

a5=turtle.Turtle()

a6=turtle.Turtle()

a7=turtle.Turtle()

a8=turtle.Turtle()

x=[a0,a1,a2,a3,a4,a5,a6,a7,a8]

xi=[a1,a2,a3,a4,a5,a6,a7,a8]

wn=turtle.Screen()

z=['yellow','red', 'blue', 'green', 'orange','purple', 'white', 'gray', 'brown', 'sea green']

j=[0.2056, 0.0068,0.0167,0.0934,0.0483,0.0560,0.0461,0.0097]

k=[0,19.5,36,50,75,130,230,300,350]

ki=[19.5,36,50,75,130,230,300,350]

for p in range(9):

    x[p].color(z[p])

    x[p].shape("circle")

    x[p].speed(0)

    x[p].up()

    x[p].goto(k[p],0)

    x[p].down()

for xx in range(10):

    for i in range(1+xx*20,21+xx*20,1):

        d=math.cos(math.radians(3.6*i))

        e=math.sin(math.radians(3.6*i))

        for yy in range(8):

            a=ki[yy]

            b=ki[yy]*math.sqrt(1-math.sqrt(j[yy]))

            xi[yy].goto(a*d,b*e)
=======
a0=turtle.Turtle()
a1=turtle.Turtle()
a2=turtle.Turtle()
a3=turtle.Turtle()
a4=turtle.Turtle()
a5=turtle.Turtle()
a6=turtle.Turtle()
a7=turtle.Turtle()
a8=turtle.Turtle()
x=[a0,a1,a2,a3,a4,a5,a6,a7,a8]
xi=[a1,a2,a3,a4,a5,a6,a7,a8]
wn=turtle.Screen()
z=['yellow','red', 'blue', 'green', 'orange','purple', 'white', 'gray', 'brown', 'sea green']
j=[0.2056, 0.0068,0.0167,0.0934,0.0483,0.0560,0.0461,0.0097]
k=[0,19.5,36,50,75,130,230,300,350]
ki=[19.5,36,50,75,130,230,300,350]
for p in range(9):
    x[p].color(z[p])
    x[p].shape("circle")
    x[p].speed(0)
    x[p].up()
    x[p].goto(k[p],0)
    x[p].down()
for xx in range(10):
    for i in range(1+xx*20,21+xx*20,1):
        d=math.cos(math.radians(3.6*i))
        e=math.sin(math.radians(3.6*i))
        for yy in range(8):
            a=ki[yy]
            b=ki[yy]*math.sqrt(1-math.sqrt(j[yy]))
            xi[yy].goto(a*d,b*e)
>>>>>>> 36c41ff1bc8e951b0c95aa1b2de28142a7ea7915
