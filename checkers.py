#Imports graphics module
from graphics import *

#Sets the max coordinates for the x and y values for the window
winX = int(900)
winY = int(900)
#Sets the width and height of each square
checkerX = int(winX / 10)
checkerY = int(winY / 10)
#Keeps track of how many sets of red and black squares are drawn in the window
rowCount = int(0)
#Counter that keeps track how many times a set of red and black squares are
#drawn on the same row
columnCount = int(0)
#Variables that keep get multiplied to the width and height of each square
#to get the correct positioning on the window
x1Count = int(1)
y1Count = int(1)
x2Count = int(2)
y2Count = int(2)
#Assigning the rgb values for black and red to the corresponding variables
black = color_rgb(0, 0, 0)
red = color_rgb(255, 0, 0)
#Counter to keep track on the color of each square
colorTrack = int(0)

#Creates the window where the hsape will be drawn
window = GraphWin("Frankie Boi's Checkerboard", winX, winY)
#Sets the lower left side of the window to be 0,0 and the upper right side
#to be 900,900
window.setCoords(0, 0, 900, 900)

#While loop to keep track of how many sets of red and black square are drawn.
#Will keep running until 32 sets of red and black squares are drawn
while rowCount < 32:
    #Creates a square using the width and height of the square multiplied by
    #the the variable x1Count, x2Count, y1Count, and y2Count
    blackChecker = Rectangle(Point(checkerX * x1Count, checkerY * y1Count),
                             Point(checkerX * x2Count, checkerY * y2Count))
    #Sets the color of the square to be black if the value of colorTrack is
    #even, and red if the value of colorTrack is odd
    if colorTrack % 2 == 0:
        blackChecker.setFill(black)
    else:
        blackChecker.setFill(red)
    #Draws the square on the window
    blackChecker.draw(window)

    #Increment each of the three variables by 1, so that the program can keep
    #track of the correct places to place the squares and the color to color it
    x1Count += 1
    x2Count += 1
    colorTrack += 1

    #Creates a square using the width and height of the square multiplied by
    #the the variable x1Count, x2Count, y1Count, and y2Count
    redChecker = Rectangle(Point(checkerX * x1Count, checkerY * y1Count),
                           Point(checkerX * x2Count, checkerY * y2Count))
    #Sets the color of the square to be red if the value of colorTrack is
    #odd, and black if the value of colorTrack is even
    if colorTrack % 2 == 1:
        redChecker.setFill(red)
    else:
        redChecker.setFill(black)
    #Draws the square on the window
    redChecker.draw(window)

    #Increment each of the three variables by 1, so that the program can keep
    #track of the correct places to place the squares and the color to color it
    x1Count += 1
    x2Count += 1
    colorTrack += 1

    #Increment each of the two variables by 1, so that the loop will create a
    #row of squares on the window, and keep track of the amount of square that
    #are already on the window
    rowCount += 1
    columnCount += 1

    #If a row is drawn, so every 4 sets of 2 squares since there are 8 squares
    #per row, then reset the variables so that they will create a new row, and
    #increment colorTrack by 1 so that the colors will alternate properly
    if columnCount == 4:
        columnCount = int(0)
        colorTrack += 1
        x1Count = int(1)
        x2Count = int(2)
        y1Count += 1
        y2Count += 1
