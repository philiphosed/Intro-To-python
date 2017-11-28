from cs1graphics import *
mytree=Canvas(500,500)
tr=Polygon(Point(0,-200),Point(100,0),Point(-100,0))
tr.setFillColor('darkGreen')
mytree.add(tr)
tr.setDepth(60)
tr.move(200,300)
oball=Circle(10,Point(200,300))
oball.setFillColor('orange')
mytree.add(oball)
oball.setDepth(10)
grball=Circle(10,Point(350,250)
grball.setFillColor('green')
mytree.add(gball)
sbball=oball.clone()
sbball.setFillColor('sky blue')
mytree.add(sbball)









