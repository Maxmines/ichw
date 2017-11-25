"""
__author__ = "huangyang"
__pkuid__  = "1700011776"
__email__  = "1700011776@pku.edu.cn"
"""
import math
import turtle
def y(a,b,c):
    for i in range(101):
        d=math.cos(math.radians(3.6*i))
        e=math.sin(math.radians(3.6*i))
        c.goto(a*d,b*e)

a0=turtle.Turtle()
a0.shape("circle")
a0.color('yellow')
wn=turtle.Screen()
z=['red', 'blue', 'green', 'orange','purple', 'white', 'gray', 'brown', 'sea green']
j=[0.2056, 0.0068,0.0167,0.0934,0.0483,0.0560,0.0461,0.0097]
k=[19.5,36,50,75,130,230,300,350]
for p in range(8):
    ap=turtle.Turtle()
    ap.color(z[p])
    ap.shape("circle")
    ap.speed(0)
    ap.up()
    ap.goto(k[p],0)
    ap.down()
    y(k[p],k[p]*math.sqrt(1-math.sqrt(j[p])),ap)