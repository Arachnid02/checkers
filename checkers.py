from graphics import *

winX = int(900)
winY = int(900)
checkerX = int(winX / 10)
checkerY = int(winY / 10)
rowCount = int(0)
x1Count = int(1)
y1Count = int(1)
x2Count = int(2)
y2Count = int(2)

window = GraphWin("Frankie Boi's Checkerboard", winX, winY)
window.setCoords(0, 0, 900, 900)

while rowCount < 4:
    blackChecker = Rectangle(Point(checkerX * x1Count, checkerY * y1Count),
                             Point(checkerX * x2Count, checkerY * y2Count))
    blackChecker.setFill(color_rgb(0, 0, 0))
    blackChecker.draw(window)
    
    x1Count += 1
    x2Count += 1

    redChecker = Rectangle(Point(checkerX * x1Count, checkerY * y1Count),
                           Point(checkerX * x2Count, checkerY * y2Count))
    redChecker.setFill(color_rgb(255, 0, 0))
    redChecker.draw(window)

    x1Count += 1
    x2Count += 1
    
    rowCount += 1
    
    print(rowCount)
