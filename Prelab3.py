from cs1graphics import *
colors=["red","blue","black","purple","yellow","orange"]
can=Canvas(500,500)
rec1=Rectangle(100,50,Point(200,30))
rec1.setFillColor(colors[0])
rec3=rec1.clone()
rec3.setFillColor(colors[2])
rec3.move(0,70)
rec6=rec3.clone()
rec6.setFillColor(colors[5])
rec6.move(0,70)
can.add(rec1)
can.add(rec3)
can.add(rec6)
