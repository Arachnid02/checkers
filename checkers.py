from graphics import *

def draw_square(sqX, sqY, sqSize, color, window):
    square = Rectangle(Point(sqX, sqY), Point(sqX + sqSize, sqY + sqSize))
    square.setFill(color)
    square.draw(window)

sqSize = 90

window = GraphWin("Frankie Boi's Checkerboard", sqSize * 10, sqSize * 10)
window.setCoords(0, 0, sqSize * 10, sqSize * 10)

for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            sqColor = "red"
        else:
            sqColor = "black"
        draw_square(sqSize * (x + 1), sqSize * (y + 1), sqSize, sqColor, window)

window.getMouse()
window.close()
