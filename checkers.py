from graphics import *

winX = int(900)
winY = int(900)
blackX = int((winX / 10) / 2)
blackY = int((winY / 10) / 2)
redX = int((winX / 10) / 2)
redY = int((winY / 10) / 2)

window = GraphWin("Frankie Boi's Checkerboard", winX, winY)
window.setCoords(0, 0, 900, 900)

blackChecker = Rectangle(Point(blackX * 2, blackY * 2),
                         Point(blackX * 4, blackY * 4))
blackChecker.setFill(color_rgb(0, 0, 0))
blackChecker.draw(window)

redChecker = Rectangle(Point(redX * 4, redY * 2),
                       Point(redX * 6, redY * 4))
redChecker.setFill(color_rgb(255, 0, 0))
redChecker.draw(window)

blackChecker = Rectangle(Point(blackX * 6, blackY * 2),
                         Point(blackX * 8, blackY * 4))
blackChecker.setFill(color_rgb(0, 0, 0))
blackChecker.draw(window)

redChecker = Rectangle(Point(redX * 8, redY * 2),
                      Point(redX * 10, redY * 4))
redChecker.setFill(color_rgb(255, 0, 0))
redChecker.draw(window)

blackChecker = Rectangle(Point(blackX * 10, blackY * 2),
                        Point(blackX * 12, blackY * 4))
blackChecker.setFill(color_rgb(0, 0, 0))
blackChecker.draw(window)

redChecker = Rectangle(Point(redX * 12, redY * 2),
                       Point(redX * 14, redY *4))
redChecker.setFill(color_rgb(255, 0, 0))
redChecker.draw(window)

blackChecker = Rectangle(Point(blackX * 14, blackY * 2),
                         Point(blackX * 16, blackY *4))
blackChecker.setFill(color_rgb(0, 0, 0))
blackChecker.draw(window)

redChecker = Rectangle(Point(redX * 16, redY * 2),
                       Point(redX * 18, redY * 4))
redChecker.setFill(color_rgb(255, 0, 0))
redChecker.draw(window)
