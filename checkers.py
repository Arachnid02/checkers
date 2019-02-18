from graphics import *

winX = int(900)
winY = int(900)
checkerX = int(winX / 10)
checkerY = int(winY / 10)
rowCount = int(0)
columnCount = int(0)
x1Count = int(1)
y1Count = int(1)
x2Count = int(2)
y2Count = int(2)
black = color_rgb(0, 0, 0)
red = color_rgb(255, 0, 0)
colorTrack = int(0)

window = GraphWin("Frankie Boi's Checkerboard", winX, winY)
window.setCoords(0, 0, 900, 900)

while rowCount < 32:
    blackChecker = Rectangle(Point(checkerX * x1Count, checkerY * y1Count),
                             Point(checkerX * x2Count, checkerY * y2Count))
    if colorTrack % 2 == 0:
        blackChecker.setFill(black)
    else:
        blackChecker.setFill(red)
    blackChecker.draw(window)
    
    x1Count += 1
    x2Count += 1
    colorTrack += 1

    redChecker = Rectangle(Point(checkerX * x1Count, checkerY * y1Count),
                           Point(checkerX * x2Count, checkerY * y2Count))
    if colorTrack % 2 == 1:
        redChecker.setFill(red)
    else:
        redChecker.setFill(black)
    redChecker.draw(window)

    x1Count += 1
    x2Count += 1
    colorTrack += 1
    
    rowCount += 1
    columnCount += 1
    
    if columnCount == 4:
        columnCount = int(0)
        colorTrack += 1
        x1Count = int(1)
        x2Count = int(2)
        y1Count += 1
        y2Count += 1
        
    print(rowCount)
