from graphics import *

def draw_square(sqX, sqY, sqSize, color, window):
    square = Rectangle(Point(sqX, sqY), Point(sqX + sqSize, sqY + sqSize))
    square.setFill(color)
    square.draw(window)

userInput = True

while userInput:
    try:
        user = input("""Do you want the program to generate your checkerboard
using preset variables? Or do you want to enter values for elements of the
checkerboard?

Type in preset to have to program generate your checkerboard using preset
values, or type in manual to enter values manually: """)
        user = user.lower()
        if user == "preset" or user == "manual":
            userInput = False
        else:
            print("\nSorry, that input is not valid. Please check your spelling.")
    except ValueError:
        print("""\nSorry, that input is not valid. Please only enter
letters. Enter preset if you want the program to generate yourcheckerboard with
preset values, or enter manual to enter values manually.""")

if user == "preset":
    sqSize = 90
    color1 = "red"
    color2 = "black"
else:
    sqSize = int(input("""\nEnter a integer value for the size of each
individual square in the checkerboard: """))
    color1 = input(""":\nEnter a color for your checkerboard. Examples are:
red,
yellow,
etc.: """)
    color2 = input(""":\nEnter a color for your checkerboard. Examples are:
red,
yellow,
etc.: """)

window = GraphWin("Frankie Boi's Checkerboard", sqSize * 10, sqSize * 10)
window.setCoords(0, 0, sqSize * 10, sqSize * 10)

for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            sqColor = color1
        else:
            sqColor = color2
        draw_square(sqSize * (x + 1), sqSize * (y + 1), sqSize, sqColor, window)

window.getMouse()
window.close()
