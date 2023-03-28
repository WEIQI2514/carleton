# Review Questions
# True/False

# 1. Using graphics.py allows graphics to be drawn in a Python shell window. F
#     Reference Page 86: "The GraphWin() function creates a new window on the screen. graphics.py is a module which is imported 
# 2. Traditionally, the upper-left comer of a graphics window has coordinates (0,0). T
#     Reference Page 88: "Traditionally, graphics programmers locate the point (0,0) in the upper-left corner of the window,"
# 3. A single point on a graphics screen is called a pixel. T
#     Reference Page 88: "A graphics winow is actually a collection of tiny points called pixels (short for 'picture elements')."
# 4. A function that creates a new instance of a class is called an accessor. F constructor
#     To create a new instance of a class, we use a special operation called a constructor. A call to a constructor is an expression that creates a brand 
#     new object."(Page 91) An accessor allows us to access information from the instance variables of the object(Page 92).

# 5. Instance variables are used to store data inside an object. T
#     Reference Page 92: Values are stored inside an object as instance variables.

# 6. The statement myShape.move(10 , 20) moves myShape to the point (10,20).F
#     Reference Page 93: All of the graphical objects have a move method specification move(dx, dy): Moves the object dx units in the x direction 
#     and dy units in the y direction.
# 7. Aliasing occurs when two variables refer to the same object. T
#     Reference Page 95: "This situation where two vairabiles refer to the same object is called aliasing."

# 8. The copy method is provided to make a copy of a graphics object. F clone
#     Reference Page 95: "The graphics library provides a better solution to copies or aliases; all graphical objects support a clone method 
#     that makes a copy of the object."

# 9. A graphics window always has the title "Graphics Window." F
#     Reference Page 98: The GraphWin constructor allows an optional parameter to specify the title of the window
#     Reference Page 113. GraphWin(title, width, height)
# 10. The method in the graphics library used to get a mouse click is read.Mouse. F
#     Reference Page 107: "When getMouse is invoked on a GraphWin, the program pauses and waits for the user to click the mouse somewhere in the graphics window."


Multiple Choice
# 1. A method that returns the value of an object's instance variable is called a(n) d
# a) mutator b) function c) constructor d) accessor*

# 2. A method that changes the state of an object is called a(n) b
# a) stator b) mutator*c) constructor d) changor

# 3. What graphics class would be best for drawing a square? d
# a) Square b) Polygon c) Line d) Rectangle*

# 4. What command would set the coordinates of win to go from (0,0) in the lower-left corner to (10, 10) in the upper-right? a
# a) win . set coords (Point (0,0), Point (10,10) )
# b) win . set coords ( (0,0), (10,10) )
# c) win . setcoords (0 , 0 , 10 , 10) *
# d) win . setcoords (Point ( 10 , 10) , Point (O , O) )

# 5. What expression would create a line from (2,3) to (4,5)?d
# a) Line (2 , 3 , 4 , 5)
# b) Line ( (2 , 3) , (4 , 5) )
# c) Line (2 , 4 , 3 , 5)
# d) Line (Point (2 , 3) , Point (4 , 5) )*  Page 90 for example

# 6. What command would be used to draw the graphics object shape into the graphics window win? d
# a) win . draw (shape) b) win . show ( shape)
# c) shape . draw ( ) d) shape . draw (win)* * Pge 115 for ref

# 7. Which of the following computes the horizontal distance between pointsp 1 and p2?b
# a) abs (p1-p2)
# b) p2.getX() - p1.getX()
# c) abs(p1.getY() - p2.getY())
# d) abs(p1.getX() - p2.getX())  *

# 8. What kind of object can be used to get text input in a graphics window? b
# a) Text b) Entry* c) Input d) Keyboard

# 9. A user interface organized around visual elements and user actions is called a(a)
# a) GUI* b) application c) windower d) API

# 10. What color is color_rgb ( 0 , 255 , 255) ? b
# a) yellow b) cyan* Page 121 c) magenta d) orange
#Yellow 	#FFFF00	255, 255, 0
#cyan     #00FFFF	0, 255, 255
#magenta  #FF00FF 255,0, 255
#orange   #FFA500	255,	65%	0%

# Discussion
#
# Q1. Pick an example of an interesting real-world object and describe it as a programming object by listing its data (attributes, what it "knows") and its methods 
#     (behaviors, what it can "do").
# A1. Objects are key to understanding object-oriented technology. You can look around you now and see many examples of real-world objects: your dog, your desk, your television
#     set, your bicycle. These real-world objects share two characteristics: They all have state and behavior. 
#     For example, dogs have state (name, color, breed, hungry) and behavior (barking, fetching, and wagging tail). 
#     For example, cats have state (name, color, breed) and behavior( purring, grooming, kneading and climbing)
#     Bicycles have state (current gear, current pedal cadence, two wheels, number of gears) and behavior (braking, accelerating, slowing down, changing gears).
#
# Q2. Describe in your own words the object produced by each of the following operations from the graphics module. Be as precise as you can. Be sure to mention such things 
#     as the size, position, and appearance of the various objects. You may include a sketch if that helps.
#
# a) Point(130, 130)
# Constructs a point at x coordinate 130 and y coordinate 130, with 0,0 being located at upper left hand corner. Page 88
#
# b) c = Circle(Point(30,40), 25)
#          c.setFill("blue")
#          c.setOutline("red")
#  A blue circle with a red outline centered at (30,40) with a radius of 25
#
# Q2c) r = Rectangle(Point(20,20), Point(40,40))
#          r.setFill(color_rgb(0,255,150)
#          r.setWidth(3)
# A square 20 units on each side centered. filled with greenish blue and the outline is 3 pixels wide black line.
#
# d) l = Line(Point(100,100), Point(100,200))
#          l.setOutline("red4")
#          l.setArrow("first")
# A vertical dark red line with an arrow to the upper point， the bottom is (100, 200) and the length is 100

# e) Oval(Point(50,50), Point(60,100))
#
# An  vertical oval 
# f) shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
#      shape.setFill("orange")
#
# two orange cross lines of length of 5sqrt2 like a x
#
# g) t = Text(Point(100,100), "Hello World!")
#          t.setFace("courier")
#          t.setSize(16)
#          t.setStyle("italic")
#          t.draw(win)
#
# A message""Hello World!" centered at (100,100), displayed in an italic size 16 "courier" font
#
#
#  Q3.  Describe what happens when the following interactive graphics program runs:
#
       from graphics import *

       def main():                          # Defines the function named main() which contains the program
           win = GraphWin()                 # Creates a GraphWin object with "Graphics Window" default title and default size 200 x 200 pixels
           shape = Circle(Point(50,50), 20) # Constructs a circle object with the center at (50,50) and radius of 20 pixels
           shape.setOutline("red")          # Calls setOutline method of circle object named shape, seting its outline to the color red
           shape.setFill("red")             # Calls setFill method of circle object shape, it fills itself with the color red
           shape.draw(win)                  # Calls draw method of circle object named shape, it draws itself in graphics window object named win
           for i in range(10):              # Creates a counted loop that will iterate 10 times
               p = win.getMouse()           # Calls getMouse() method of graphics window object win, pauses program for user to click in win, returns mouse click as Point object,
                                            # which is assigned to the variable p (an event object)
               c = shape.getCenter()        # Calls getCenter() method of circle object shape, returns a clone of the center point of shape
               dx = p.getX() - c.getX()     # Assignment statement whereby variable dx is assigned the expression in the getX() methods of p and c are used to calculate the
                                            # difference along the x axis of the user's mouse click with respect to the center point of shape
               dy = p.getY() - c.get&()     # Assignment statement whereby variable dy is assigned a similar expression as dx, except this time it is for the Y axis
               shape.move(dx, dy)           # Calls the move() method of shape to move shape by the x distance referred to by dx and the y distance referred to by dy, thus
                                            # Moves the red circle shape moving its center point to the new coordinates encapsulated in the event object p
          win.close()                       # Calls the close() method of the Graphics Window variable win, closing the graphics window after the loop is finished.
                                            # Note that it will not be possible to see the final location of the circle. To do so, comment out win.close() or call on win's
                                            # getMouse() method to make win close after a mouse click.
       main()                               # Calls the function named main() to run the program


# Programming Exercises
#
# Q1a) Alter the previous program to draw squares rather than circles
#
# Programming Exercises

# 1. Alter the program from the last discussion question in the following ways:
# a) Alter the previous program to draw squares rather than circles

from graphics import * 

def main() : 
    win = GraphWin() 
    shape = Rectangle (Point(50,50),  Point(70,70))
    shape.setOutline ("red") 
    shape.setFill ("red") 
    shape.draw(win) 
    for i in range (10) : 
        p = win.getMouse () 
        c = shape.getCenter()
        dx = p.getX () - c.getX ()
        dy = p.getY() - c.getY() 
        shape.move (dx,dy)
    win.close()
    
main()

# b) Have each successive click draw an additional square on the screen (rather than moving the existing one).
from graphics import * 

def main() : 
    win = GraphWin() 
    shape = Rectangle (Point(50,50), Point(70,70))
    shape.setOutline ("red") 
    shape.setFill ("red" ) 
    shape.draw(win) 
    for i in range (10) : 
        p = win.getMouse () 
        c = shape.getCenter()
        dx = p.getX () - c.getX ()
        dy = p.getY() - c.getY() 
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    win.close()
    
main()

# Q1c Print a message on the window "Click again to quit" after the loop, and wait for a final click before closing the window. Insert immediately before win.close():
#import graphics
from graphics import * 
def main() : 
    win = GraphWin() 
    shape = Rectangle (Point(50,50), Point(70,70))
    shape.setOutline ("red") 
    shape.setFill ("red" ) 
    shape.draw(win) 
    for i in range (10) : 
        p = win.getMouse () 
        c = shape.getCenter()
        dx = p.getX () - c.getX ()
        dy = p.getY() - c.getY() 
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
       
    message = Text (Point (100,50 ) , "Click again to quit!") 
    message.draw(win)
    Text(Point(100,180), "Click again to quit.").draw(win)
    win.getMouse ()
    win.close()
    
main()

# Q2) An archery target consists of a central circle of yellow surrounded by concentric rings of red, bue, black and white. Each ring has the same width, which is the same as 
#     the radius of the yellow circle. Write a program that draws such a target.
#     Hint: Objects drawn later will appear on top of objects drawn earlier
#
# Archery target
import graphics
from graphics import * 

def main() : 
    win = GraphWin("Archery Target") 
    center = Point (100 , 100)
    Whitecir = Circle (center, 100) 
    Whitecir.setOutline ("black") 
    Whitecir.setFill ("white" ) 
    Whitecir.draw(win) 
    
    Blackcir = Circle (center, 80) 
    Blackcir.setOutline ("black") 
    Blackcir.setFill ("black" ) 
    Blackcir.draw(win)
    
    Bluecir = Circle （center, 60) 
    Bluecir.setOutline ("blue") 
    Bluecir.setFill ("blue" ) 
    Bluecir.draw(win)
    
    Redcir = Circle (center, 40) 
    Redcir.setOutline ("red") 
    Redcir.setFill ("red" ) 
    Redcir.draw(win)
    
    Centercir = Circle (center, 20) 
    Centercir.setOutline ("yellow") 
    Centercir.setFill ("yellow" ) 
    Centercir.draw(win)
    
    Text (center, "Click again to quit!") .draw(win)
    win.getMouse ()
    win.close ()
    
main()

# Q3) Write a program which draws some sort of face
#
#
import graphics
from graphics import *

def main():
    #head
    win = GraphWin('Face',400,400)
    f = Oval(Point(85,75),Point(315,325))
    f.setFill('Lavender Blush')
    f.draw(win)

    #eyes
    el = Circle(Point(160,160),15)
    el.setFill('white')
    el.draw(win)
    ebl = Circle(Point(160,160),5)
    ebl.setFill('black')
    ebl.draw(win)

    er = Circle(Point(240,160),15)
    er.setFill('white')
    er.draw(win)
    ebr = Circle(Point(240,160),5)
    ebr.setFill('black')
    ebr.draw(win)

    #mouth
    n = Oval(Point(170,250),Point(230,270))
    n.setFill('pink')
    n.draw(win)
    l = Line(Point(170,260),Point(230,260))
    l.draw(win)
    
    #nose
    n = Polygon(Point(200,150),Point(180,240),Point(220,240))
    n.setFill('pink')
    n.draw(win)

    win.getMouse() # pause for click in window
    win.close()

main()


# Q4) Write a program which draws a winter scene with a Christmas tree and snowman
#
#Write a program that draws a winter scene and some snowmen.
import graphics
from graphics import *

def main():
    #head
    win = GraphWin('winter scene',600,450)

    #background
    win.setBackground('darkgrey')

    #snow
    sn = Rectangle(Point(0,170), Point(600,450))
    sn.setFill('white')
    sn.draw(win)

    #trees
    tr = Polygon(Point(50,300), Point(120,210), Point(200,300))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(65,220), Point(120,130), Point(175,220))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(80,140), Point(120,85), Point(160,140))
    tr.setFill('green')
    tr.draw(win)
    
    tr = Rectangle(Point(116,320),Point(124,300))
    tr.setFill('black')
    tr.draw(win)

    tr = Polygon(Point(400,350), Point(450,280), Point(500,350))
    tr.setFill('green')
    tr.draw(win)
    
    tr = Polygon(Point(410,300), Point(450,230), Point(490,300))
    tr.setFill('green')
    tr.draw(win)
    
    tr = Polygon(Point(420,250), Point(450,180), Point(480,250))
    tr.setFill('green')
    tr.draw(win)
    
    tr = Rectangle(Point(446,370),Point(454,350))
    tr.setFill('black')
    tr.draw(win)
    
    #snowman
    s = Circle(Point(300,300),80)
    s.setFill('white')
    s.draw(win)

    s = Circle(Point(300,210),50)
    s.setFill('white')
    s.draw(win)

    s = Circle(Point(300,145),45)
    s.setFill('white')
    s.draw(win)

    #coal
    c = Circle(Point(280,135),7)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(320,135),7)
    c.setFill('black')
    c.draw(win)

    #carrot
    c = Circle(Point(300,150),5)
    c.setFill('orange')
    c.draw(win)
    
    c = Polygon(Point(300,155),Point(300,145),Point(270,154))
    c.setFill('orange')
    c.draw(win)


    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q5) Write a program that draws 5 dice on the screen depicting a straight (1,2,3,4,5 or 2,3,4,5,6).
#
#Write a program that draws 5 dice on the screen depicting a straight (1, 2, 3, 4, 5)
import graphics
from graphics import *

def main():
    win = GraphWin('dice',500,100)
    win.setCoords(0,0,5,1)

    for i in range(5):
        dice = Rectangle(Point(0.1+i,0.1),Point(0.9+i,0.9))
        dice.setFill('red')
        dice.draw(win)

    center = Point((0.5),(0.5))

    #dice1
    d1 = Circle(center,0.08)
    d1.setFill('white')
    d1.setOutline('white')
    d1.draw(win)

    #dice2
    d2a = d1.clone()
    d2a.draw(win)
    d2a.move(0.8,0.2)

    d2b = d1.clone()
    d2b.draw(win)
    d2b.move(1.2,-0.2)

    #dice3
    d3a = d1.clone()
    d3a.draw(win)
    d3a.move(2.0,0.0)

    d3b = d1.clone()
    d3b.draw(win)
    d3b.move(2.2,0.2)

    d3c = d1.clone()
    d3c.draw(win)
    d3c.move(1.8,-0.2)

    #dice4
    d4a = d1.clone()
    d4a.draw(win)
    d4a.move(2.8,-0.2)

    d4b = d1.clone()
    d4b.draw(win)
    d4b.move(2.8,0.2)

    d4c = d1.clone()
    d4c.draw(win)
    d4c.move(3.2,0.2)

    d4d = d1.clone()
    d4d.draw(win)
    d4d.move(3.2,-0.2)

    #dice5
    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.0,0.0)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.8,-0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.8,0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.2,0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.2,-0.2)

    win.getMouse() # pause for click in window
    win.close()

main()
#
#Write a program that draws 5 dice on the screen depicting a straight ( 2, 3, 4, 5, 6)
import graphics
from graphics import *

def main():
    win = GraphWin('Dices2',500,100)
    win.setCoords(0,0,5,1)

    for i in range(5):
        dice = Rectangle(Point(0.1+i,0.1),Point(0.9+i,0.9))
        dice.setFill('white')
        dice.draw(win)

    center = Point((0.5),(0.5))
    # dice 0- 1 points
    d1 = Circle(center,0.08)
    d1.setFill('red')

    #dice1-2 points
    d2a = d1.clone()
    d2a.draw(win)
    d2a.move(-0.2,0.2)

    d2b = d1.clone()
    d2b.draw(win)
    d2b.move(0.2,-0.2)

    #dice2 - 3points
    d3a = d1.clone()
    d3a.draw(win)
    d3a.move(1.0,0.0)

    d3b = d1.clone()
    d3b.draw(win)
    d3b.move(0.8,0.2)

    d3c = d1.clone()
    d3c.draw(win)
    d3c.move(1.2,-0.2)

    #dice3 -4 points
    d4a = d1.clone()
    d4a.draw(win)
    d4a.move(1.8,-0.2)

    d4b = d1.clone()
    d4b.draw(win)
    d4b.move(1.8,0.2)

    d4c = d1.clone()
    d4c.draw(win)
    d4c.move(2.2,0.2)

    d4d = d1.clone()
    d4d.draw(win)
    d4d.move(2.2,-0.2)

    #dice4-5 points
    d5a = d1.clone()
    d5a.draw(win)
    d5a.move(3,0.0)

    d5b = d1.clone()
    d5b.draw(win)
    d5b.move(2.8,-0.2)

    d5c = d1.clone()
    d5c.draw(win)
    d5c.move(2.8,0.2)

    d5d = d1.clone()
    d5d.draw(win)
    d5d.move(3.2,0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.2,-0.2)
    
    #dice5 -6 points
    d6a = d1.clone()
    d6a.draw(win)
    d6a.move(3.8,0.2)

    d6b = d1.clone()
    d6b.draw(win)
    d6b.move(3.8,0.0)

    d6c = d1.clone()
    d6c.draw(win)
    d6c.move(3.8,-0.2)
    
    d6d = d1.clone()
    d6d.draw(win)
    d6d.move(4.2,0.0)

    d6e = d1.clone()
    d6e.draw(win)
    d6e.move(4.2,0.2)

    df = d1.clone()
    d6f.draw(win)
    d6f.move(4.2,-0.2)

    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q6) Modify the graphical future value program so that the input (principal and APR) also are done in a graphical fashion using Entry objects.
#
#futval_graph.py
from graphics import *

def main():
    
    #Introduction
    print("The program plots the growth of a 10-year investment")

    #Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-9000, 11.5,15400)

    #Principle input
    Text(Point(1.0, -2000), "Input starting principle").draw(win)
    inputprinciple = Entry(Point(3.2, -2000), 6)
    inputprinciple.setText("0")
    inputprinciple.draw(win)

    #Interest input
    Text(Point(7, -2000), "Input interest rate(%)").draw(win)
    inputinterest = Entry(Point(9.5, -2000),6)
    inputinterest.setText("0")
    inputinterest.draw(win)

    #Create the Calculate button
    button = Rectangle(Point(2,-6000),Point(8,-8000))
    button.setFill("blue")
    button.draw(win)
    buttontxt = Text(Point(5,-7200),"Calculate:")
    buttontxt.draw(win)
    win.getMouse()

    #Receive input
    p = eval(inputprinciple.getText())
    q = eval(inputinterest.getText())/100

    #labels
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)
    Text(Point(4.0, 14000), "Future Values Calculator").draw(win)
         
    #Draw a bar for the initial principle
    bar = Rectangle(Point(0, 0), Point(1, p))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw bars for successive years
    for i in range(1,11):
        #calculate value for next year
        p = p * (1 + q)
        #Draw a bar for this value
        bar = Rectangle(Point(i, 0), Point(i+1, p))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    buttontxt.setText('Quit.')

    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q7) Circle Intersection.
#     Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#     Input: Radius of the circle and the y-intercept of the line.
#     Output: Draw a circle centered at (0,0) with teh given radius in a window with coordinates running from -10,-10 to 10,10.
#     Draw a horizontal line across the window and the given-y intercept.
#     Draw the two points of intersection in red.
#     Print out the x values of the points of intersection.
#     Formula: x = + or -(sqrt((r^2 = y^2))
#
#
from graphics import *
from math import sqrt

def main():
    win = GraphWin('Circle Intersetion',400,400)
    win.setCoords(-10,-12,10,10)
    
    #step 1: description
    descr = Text(Point(0,8),"Program to calculate x value intersections")
    click = Text(Point(0,-11), "Click anywhere to continue")
    descr.setSize(8)
    click.setSize(8)
    descr.draw(win)
    click.draw(win)
    
    win.getMouse() # Wait for mouse click and then clear screen
    descr.undraw()
    
    #step 2: Obtain input from user
    #Add entry box for radius and y intercept
    r_text = Text(Point(-4,4),"Radius:")
    y_text = Text(Point(-4,2),"Intersection:")
    r_text.setSize(8)
    y_text.setSize(8)
    r_text.draw(win)
    y_text.draw(win)
    r_input = Entry(Point(0,4), 3)
    y_input = Entry(Point(0,2), 3)
    r_input.setSize(8)
    y_input.setSize(8)
    r_input.draw(win)
    y_input.draw(win)
    
    #Get the radius and intercept from the user and clear screen
    win.getMouse()
    r = eval(r_input.getText())
    y = eval(y_input.getText())
    r_text.undraw()
    y_text.undraw()
    r_input.undraw()
    y_input.undraw()
    click.undraw()
    
    #Compute the x values of intersection
    x_int1 = -sqrt(r ** 2 - y ** 2)
    x_int2 = sqrt(r ** 2 - y ** 2)
    
    
    #Step 3: Displaying data
    # Draw circle and line on the x and y axis
    x_axis = Line(Point(-10,0), Point(10,0))
    x_axis.setArrow("last")
    y_axis = Line(Point(0,-10), Point(0,10))
    y_axis.setArrow("last")
    circ = Circle(Point(0,0), r)
    
    line = Line(Point(-10,y), Point(10, y))
    
    int1 = Circle(Point(x_int1, y), 0.2)
    int1.setFill("red")
    int1.setOutline("red")
    int2 = Circle(Point(x_int2, y), 0.2)
    int2.setFill("red")
    int2.setOutline("red")
    x_axis.draw(win)
    y_axis.draw(win)
    circ.draw(win)
    line.draw(win)
    int1.draw(win)
    int2.draw(win)
    
    #Dispay the x_int on screen
    x1_text = Text(Point(x_int1-2,y+0.5), f"x1 are {round(x_int1)}")
    x2_text = Text(Point(x_int2+2,y+0.5), f"x2 are {round(x_int2)}")
    int_info = Text(Point(0,-11), f" x points are {x_int1} and {x_int2}")
    x1_text.setSize(8)
    x2_text.setSize(8)
    x1_text.draw(win)
    x2_text.draw(win)
    int_info.setSize(8)
    int_info.draw(win)

    
    win.getMouse()#Close the window by clicking the mouse
    win.close()

main()
#
# Q8) Line Segment Information.
#     This program allows the suer to draw a line segment that then displays some graphical and textual information about the line segment.
#     Input: Two mouse clicks for the end points of the line segment.
#     Output: Draw the midpoint of the segment in cyan.
#             Draw the line.
#             Print the length and the slope of the line.
#     Formulas: dx = x2 - x1
#               dy = y2 - y1
#               slope = dy / dx
#               length = sqrt(dx^2 + dy^2)
#
from graphics import *
from math import * # You can also do import math

def main():
    win = GraphWin("Line drawing tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    
    message = Text(Point(0, 8), "Click on 2 points to create a line")#Prompt the user for 2 mouse clicks
    message.setFill("blue")
    message.draw(win)
    
    #Store the co-ordinates in variables x1 and x2
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    print(x1)
    print(x2)
    print(y1)
    print(y2)
    
    #Create a line with midpoint as "cyan"
    line = Line(point1,point2)
    line.draw(win)
    mx = (x1+x2)/2
    my = (y1+y2)/2
    print(mx)
    print(my)
    win.plot(mx, my, "red")
    
    #Print the length and slope of the line
    dx = x2 - x1
    dy = y2 - y1
    slope = dy /dx
    print("The slope of the slope is: ", round(slope,2))
    message2 = Text(Point(0, -6), ("The slope of the line is: ", round(slope,2)))
    message2.draw(win)
    #Print the length of the line
    length = sqrt(dx**2 + dy**2)
    print("The length of the line is", round(length, 2))
    message3 = Text(Point(0, -3), ("The length of the line is: ", round(length,2)))
    message3.draw(win)
    
    win.getMouse()#Close the window by clicking the mouse
    win.close()
    
main()
#
# Q9) Rectangle Information.
#     This program displays information about a rectangle drawn by the user.
#     Input: Two mouse clicks for the opposite corners of a rectangle.
#     Output: Draw the rectangle.
#             Print the perimeter and area of the rectangle.
#     Formulas: area = (length)(width)
#               perimeter = 2(length + width)
#
#This program displays information about a triangle draw by the user

#Q9 Rectangle.py
from graphics import *
import math

def main():
    win = GraphWin("Rectangle drawing tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    
    message = Text(Point(0, 8), "Click on 2 points to create a Rectangle")#Prompt the user for 2 mouse clicks
    message.setFill("green")
    message.draw(win)
    
    #Store the co-ordinates in variables x1 and x2
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    print(x1)
    print(x2)
    print(y1)
    print(y2)
    
    
    rect = Rectangle(Point(x1,y1),Point(x2,y2))
    rect.draw(win)
    
    
    #Print the length and perimeter of the Rectangle
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    area = length * width
    print("The area of the Rectangle is: ", round(area,2))
    message2 = Text(Point(0, -6), ("The area of the Rectangle is: ", round(area,2)))
    message2.draw(win)
    #Print the perimeter of the Rectangle
    perimeter = 2 * (length + width)
    print("The perimeter of the rectangle is", round(perimeter, 2))
    message3 = Text(Point(0, -3), ("The perimeter of the rectangle is: ", round(perimeter,2)))
    message3.draw(win)
    
    win.getMouse()#Close the window by clicking the mouse
    win.close()
    
main()
#
#
# Q10)Triangle Information.
#     Same as the previous problem, but with three clicks for the vertices of the triangle.
#     Formulas: For perimeter, see length fromt he Line Segment problem.
#     area = sqrt(s(s - a)(s - b)(s - c)) where a, b, and c are the lengths of the sides and s = (a + b + c) / 2.
#
#This program displays information about a triangle draw by the user
def main():
    win = GraphWin("Triangle drawing tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    
    message = Text(Point(0, 8), "Click on 3 points to create a Triangle")#Prompt the user for 2 mouse clicks
    message.setFill("blue")
    message.draw(win)
    
    #Store the co-ordinates in variables x1,x2 and x3
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    x3 = point3.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    y3 = point3.getY()
    print(x1)
    print(x2)
    print(x3)
    print(y1)
    print(y2)
    print(y3)
    
    
    tri = Polygon(Point(x1,y1),Point(x2,y2), Point(x3,y3))
    tri.draw(win)
    
    
    #Print the length and perimeter of the Triangle
    a = sqrt((y2-y1)**2 + (x2-x1)**2)
    b = sqrt((y3-y2)**2 + (x3-x2)**2)
    c = sqrt((y3-y1)**2 + (x3-x1)**2)
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) *(s - b) * (s - c))
    print("The area of the Triangle is: ", round(area,2))
    message2 = Text(Point(0, -6), ("The area of the Triangle is: ", round(area,2)))
    message2.draw(win)
    #Print the perimeter of the Rectangle
    perimeter = 2 * s
    print("The perimeter of the Triangle is", round(perimeter, 2))
    message3 = Text(Point(0, -3), ("The perimeter of the Triangle is: ", round(perimeter,2)))
    message3.draw(win)
    
    win.getMouse()#Close the window by clicking the mouse
    win.close()
    
main()
#
#
# Q11) Five-click House.
#     You are to write a program that allows the user to draw a simple house using five mouse clicks. The fisrt two clicks will be the opposite
#     corners of the rectangular frame of the house. The third click will indicate the center of the otp ege of a rectangular door. The door should
#     have a total width that is 1/5 the wdith of the house frame. The sides of the door should have extend from the corners of the top down to the
#     bottom of the frame. The fourth click will indicate the center of a square window. The window is half as wide as the door. The last click will
#     indicate the peak of the roof. The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.
#
#This program draws a simple house using 5 mouse clicks
def main():
    win = GraphWin("Drawing a simple house in 5 mouse clicks", 400, 400)
    win.setCoords(0, 0, 20, 20)
    
    
    message = Text(Point(0, 2), "Click on 2 points to create a frame")#Prompt the user for 2 mouse clicks
    message.setFill("blue")
    message.draw(win)
    
    #Store the co-ordinates in variables x1,x2 and x3
    point1 = win.getMouse()
    point2 = win.getMouse()
    
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    
    frame = Rectangle(point1,point2)
    frame.draw(win)
    message.undraw()
    
    message2 = Text(Point(15, 15), "Click on 3rd point to create a door")
    message2.setFill("blue")
    message2.draw(win)
    
    point3 = win.getMouse()
    x3 = point3.getX()
    y3 = point3.getY()
    
    
    w_door = (x1-x2) * 1/5
    
    door = Rectangle(Point((x3-(w_door/2)),y1),Point((x3+(w_door/2)),y3))
    door.draw(win)
    message2.undraw()
    
    message3 = Text(Point(15, 15), "Click on 3rd point to create a window")
    message3.setFill("blue")
    message3.draw(win)
    
    point4 = win.getMouse()
    x4 = point4.getX()
    y4 = point4.getY()
    print(x4)
    print(y4)
    
    w_window = w_door * 1/2
    atr =w_window * 1/2
    
    window = Rectangle(Point((x4-atr),(y4-atr)),Point((x4+atr),(y4+atr)))
    window.draw(win)
    message3.undraw()
    
    message4 = Text(Point(15, 15), "Click on 3rd point to create the roof")
    message4.setFill("blue")
    message4.draw(win)
    
    point5 = win.getMouse()
    x5 = point5.getX()
    y5 = point5.getY()
    print(x5)
    print(y5)
    
    tri = Polygon(Point(x1,y2),Point(x2,y2), Point(x5,y5))
    tri.draw(win)
    message4.undraw()
    
    win.getMouse()#Close the window by clicking the mouse
    win.close()
    
main()
