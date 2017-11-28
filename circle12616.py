color=['red','yellow','green']
radius=[49,100,200]
from cs1graphics import *
can=Canvas(500,500)
yc=Circle(radius[1],Point(100,100))
yc.setFillColor(color[1])
can.add(yc)
gc=Circle(radius[2],Point(200,450))
gc.setFillColor(color[2])
can.add(gc)
rc=Circle(radius[0],Point(450,250))
rc.setFillColor(color[0])



