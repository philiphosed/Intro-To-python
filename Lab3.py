from cs1graphics import *
colors=list()
colors1=raw_input("Enter 1st color:") #this was made to set for bonus
colors.append(colors1)
colors2=raw_input("Enter 2nd color:") #this was made to set for bonus
colors.append(colors2)
colors3=raw_input("Enter 3rd color:") #this was made to set for bonus
colors.append(colors3)
corodin=[100,90,200,70,90,400,250,130,108,430,304,49]
can=Canvas(500,500)
c1=Circle(50,Point(corodin[0],corodin[1]))
c1.setFillColor(colors[0])
c2=c1.clone()
c2.move(0,100)
c2.setFillColor(colors[1])
c3=c2.clone()
c3.move(0,100)
c3.setFillColor(colors[2])
cAll=[c1,c2,c3]
can.add(c1)
can.add(c2)
can.add(c3)
from time import sleep
timeDelay = .50
cAll[0].setFillColor(colors[2])
cAll[1].setFillColor(colors[0])
cAll[2].setFillColor(colors[1])
sleep(timeDelay)
cAll[0].setFillColor(colors[1])
cAll[1].setFillColor(colors[2])
cAll[2].setFillColor(colors[0])
sleep(timeDelay)
cAll[0].setFillColor(colors[0])
cAll[1].setFillColor(colors[1])
cAll[2].setFillColor(colors[2])
sleep(timeDelay)
cAll[0].setFillColor(colors[2])
cAll[1].setFillColor(colors[0])
cAll[2].setFillColor(colors[1])
sleep(timeDelay)
cAll[0].setFillColor(colors[1])
cAll[1].setFillColor(colors[2])
cAll[2].setFillColor(colors[0])
sleep(timeDelay)
cAll[0].setFillColor(colors[0])
cAll[1].setFillColor(colors[1])
cAll[2].setFillColor(colors[2])
sleep(timeDelay)
cAll[0].setFillColor(colors[2])
cAll[1].setFillColor(colors[0])
cAll[2].setFillColor(colors[1])


