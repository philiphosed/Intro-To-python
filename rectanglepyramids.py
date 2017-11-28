from cs1graphics import *
numLevels = 20
unitSize = 12
screenSize = unitSize * (numLevels + 1)
paper = Canvas(screenSize, screenSize)
centerX = screenSize/2.0
for level in range(numLevels): #create top to bottom levels.
    width = (level + 1)* unitSize
    block = Rectangle(width, unitSize)
    centerY = (level + 1) * unitSize
    block.move(centerX, centerY)
    block.setFillColor('grey')
    paper.add(block)
