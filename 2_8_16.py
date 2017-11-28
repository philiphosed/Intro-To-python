from cs1graphics import *
screen=Canvas(1000,1000)
radius=50
colors=['red','green']
i=0
for i in range(5):
    c=Circle(radius,Point(100,100))
    screen.add(c)
    radius=radius+50
    if i%2==0:
        c.setFillColor(colors[0])
    else:
        c.setFillColor(colors[1])
        i=i+1
