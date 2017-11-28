from cs1graphics import *
mycan=Canvas(200,200)
colors=['blue','green']
x=0
for i in range(8):
    s=Square(30)
    mycan.add(s)
    sqaure.moveTo(50+x,50)
    if i%2==0:
        s.setFillColor(colors[0])
    else:
        s.setFillColor(colors[1])
    x+=30
    

    
