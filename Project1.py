#David Philiphose
#philiphosed@slu.edu
#2/3/16
#CSCI 1300-01
#Instructor: Judy Etchison
from cs1graphics import *     #this imports cs1graphics
mycan=Canvas(500,500,"white","Hot Air Balloon")
boat=Layer()                  #builds boat layer
mast=Rectangle(7,150)
mast.setFillColor('brown')
boat.add(mast)
sail1=Polygon(Point(0,50),Point(39,-100),Point(90,0))
sail1.rotate(27)
sail1.move(-115,-10)
sail1.setFillColor('white')
sail2=sail1.clone()
sail2.move(228,0)
sail2.flip()
hull2=Rectangle(200,30)
hull2.move(0,90)
hull2.setFillColor('red')
boat.add(hull2)
boat.add(sail2)
boat.add(sail1)
mycan.add(boat)             #this adds boat to the canvas
boat.move(400,350)
boat.scale(.25)             #this shrinks down the boat
sky1=Rectangle(500,300)
sky1.setFillColor('skyblue')
sky1.move(250,100)
mycan.add(sky1)              #adds sky to the canvas
sky1.setDepth(70)
sky1.setBorderColor('skyblue')
sky2=sky1.clone()            #clones sky to make the ocean
sky2.move(0,300)
mycan.add(sky2)
sky2.setFillColor('blue')
balloon=Layer()               #this builds layer for balloon
b1=Circle(40,Point(0,0))
balloon.add(b1)
mycan.add(balloon)
balloon.setDepth(30)
balloon.move(100,100)
b1.setFillColor('orange')
b2=Polygon(Point(-40,0),Point(-20,85),Point(20,85),Point(40,0))
balloon.add(b2)
b2.setFillColor('orange')
b1.setBorderColor('orange')
b2.setBorderColor('orange')
b2.move(0,6)
rope1=Rectangle(7,90)
balloon.add(rope1)
rope1.setDepth(60)
rope1.setFillColor('brown')
rope1.move(-15,100)
rope2=rope1.clone()
rope2.move(30,0)
balloon.add(rope2)
basket=Square(40,Point(0,150))
balloon.add(basket)
basket.setFillColor('brown')
start=Text('Click to see boat and balloon move',12,Point(250,300)) #this adds display to give user a prompt
mycan.add(start)
mycan.wait()
start.setDepth(100)
from time import sleep      #adds delay for animation
timeDelay=(.25)
balloon.move(20,0)
boat.move(-10,0)
sleep(timeDelay)
balloon.move(30,0)
boat.move(-20,0)
sleep(timeDelay)
balloon.move(40,0)
boat.move(-30,0)
sleep(timeDelay)
balloon.move(50,0)
boat.move(-40,0)
sleep(timeDelay)
balloon.move(60,0)
boat.move(-50,0)
sleep(timeDelay)















