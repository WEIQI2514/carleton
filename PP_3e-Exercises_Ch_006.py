# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 6: Defining Functions
# End-of-Chapter Exercises

# Review Questions

# True/False
# 1. Programmer srarely define their own functions  False
# 2. A function can only be called at once place in a program = False
# 3. Information can be passed into a function through parameters  True
# 4. Every Python function returns some value = True (None is returned when no explicit value is provided)
# 5. In Python, some parameters are passed by reference = False. Page 195. Technically Python passes all parameters by value
# 6. In Python a function can return only one value = False. Page 203
# 7. Python functions can never modify a parameter = False. Page 193/198/199. Parameters are always passed by value. However if the actual parameter is a variable whose 
#    object is a mutable object like a list, then changes to the object will be visible to the other program.
# 8. One reason to use functions is to reduce code duplication = True.
# 9. Variables defined in a function are local to that function = True. Page 203. Formal parameters and other variables inside fucntion definitions are local to that 
#    function
# 10. It's a bad idea to define new functions if it makes a program longer = False. Although some programs look longer it makes it much easier for experienced programmers
#     to understand
#
Multiple Choice 
1. The part of a program that uses a function is called the 
a) user b) caller* c) callee d) statement 
2. A Python function definition begins with 
a) def* b) define c) function d) defun 
3. A function can send output back to the program with a(n) 
a) return* b) print c) assignment d) SASE 
4. Formal and actual parameters are matched up by 
a) name b) position* c) ID d) interests 
5. Which of the following is not a step in the function-calling process? 
a) The calling program suspends. 
b) The formal parameters are assigned the value of the actual parameters. 
c) The body of the function executes. 
d) Control returns to the point just before the function was called. *
6. In Python, actual parameters are passed to functions 
a) by value* b) by reference c) at random d) by networking 
7. Which of the following is not a reason to use functions? 
a) to reduce code duplication 
b) to make a program more modular 
c) to make a program more self-documenting 
d) to demonstrate intellectual superiority *
8. If a function returns a value, it should generally be called from 
a) an expression* b) a different program c) main d) a cell phone 
9. A function with no return statement returns 
a) nothing b) its parameters c) its variables d) None *
10. A function can modify the value of an actual parameter only if it's 
a) mutable* b) a list c) passed by reference d) a variable

Discussion 
# Q1. In your own words, describe two motivations for defining functions in your programs
# A1: functions are useful for me to avoid replicate coding and it make the code more readable and modular. better way to keep the code sync .

# Q2. We have been thinking about computer programs as sequences of instructions where the computer methodically executes one instruction and then moves on to the next
#     one. Do programs that contain functions fit this model.

# A2. In a sense a script always travels downwards, it just uses references to functions listed as it moves through the scripts so it may look like it is going backwards 
#     and forwards but in fact, it is just referring to a pre created command. A bit like a journey where you keep going forwards, you just refer to the map every now 
#     and again

# Q3
# a). Parameters are an important concept in defining functions. What is the purpose of parameters?
 
# A3a. parameters passes the value from functions. The only way for a function to see a variable from another function is for the variable to be passed as a parameter

# b). What is the difference between a formal parameter and an actual parameter?

# A3b. The parameter appearing in the function definition is called the formal parameter and the expressions appearing in a function call are known as the actual 
#      parameters
#
# c). In what ways are parameters similar to and different from ordinary variables?

# A3c. Parameters are like ordinary function variables in that they are local to the function and serve as "named values." They are different because they are 
#      automatically assigned an initial value when the function is called. Normal local variables have to be assigned a value within the function definition.

# Q4.  Functions can be thought of as miniature (sub) programs inside other programs. Like any other program, we can think of functions as having input and output to 
#      communicate with the main program.
   a). How does the program provide "input" to one of it's functions?
# A4a. A program provides input by parameters

# b).  How does a function provide output to the program?
# A4b. Usually through a return statement. Functions may also change the values of mutable parameters

# Q5a. Consider this simple function. What does thsi function do?
       def cube(x):
          answer = x * x * x
          return answer
# a). This function computes the cube of x
# b). Show how a program could use this function to print the value of y(3)
      def cube(y)
# c). Here is a fragment of the program that uses this function. The output from this function is 4 27. Explain why the output is not 27 27 even though the cube seems to
#      to change the value of the answer to 27.
#      answer = 4
       result = cube(3)
       print(answer, result)
# A5c. There are two different variables named answer. The variable inside of cube is changed, but it does not affect the value of the other variable.

# Programming Exercises

# Exercise 1

# Write a program to print the lyrcis of "Old McDonald had a Farm for 5 different animals

#Old McDonald had a Farm

def lyrics1():
    print( "Old McDonald had a farm,Ee-igh, Ee-igh, Oh!")

def verse(animal, noise):
    print("And on that farm he had a "+ animal +" Ee-igh, Ee-igh, Oh!")
    print("With a {0}, {0} here and a {0}, {0} there.".format(noise) )
    print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(noise) )

def om(animal,noise):
    lyrics1()
    verse(animal,noise)
    lyrics1()
    print()
    
def main():
    om("horse", "neigh")
    om("duck", "quack")
    om("sheep", "mia")
    om("cow", "moo")
    om("dog", "woof")
main()

# Exercise 2

# Write a program to print the lyrics for ten verses of "The ant's go marching in

# The ants go marching in

def line():
    print("And they all go marching down ... ")
    print("In the ground ...")
    print("To get out ....")
    print("Of the rain")
    print("Boom! Boom! Boom!")

def ants():
    num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    rhyme = ['suck his thumb','tie his shoe','brush his hair', 'shut the door','dance like crazy','pick up stones', 'eat the grass','make a cake', 'eat a bug', 'chase the cat']
    for i in range(10):
        print("The ants go marching {0} by {0},hurrah! hurrah!".format(str(num[i])))
        print("The ants go marching {0} by {0},hurrah! hurrah!".format(str(num[i])))
        print("The ants go marching {0} by {0},".format(str(num[i])))
        print("The little one stops to {},".format(rhyme[i]))
        line()
        print()
    
def main():
    ants()
main()

# Exercise 3

# Write definitions for these functions

# sphereArea(radius) Returns the surface area of a sphere having a given radius

# Calculating the radius of a sphere
import math

def sphereArea(radius):
    return 4 * math.pi* radius **2
   
def sphereVolume(radius):
    return 4/3 * math.pi * radius **3

def main():
    r = float(input("Enter the radius of the sphere: "))
    print("The area of the sphere is", sphereArea(r))
    print()
    print("The volume of a sphere is", sphereVolume(r))

main()

# Exercise 4

# Write definitions for the following two functions

# sumN(n) returns the sum of the first n natural numbers
def sumN(n):
    total = 0
    for i in range(n + 1):
        total = total + i 
    return total

# sumNCubes(n) returns the sum of the cubes of the first n natural numbers
def sumNCubes(n):
    total = 0
    for i in range(n + 1):
        total = total + i**3 
    return total

def main():
    n = int(input("Enter an integer: "))
    print("The sum of {0} is {1}".format(n, sumN(n)))
    print()
    print("The sum of {0} cubes is {1}".format(n, sumNCubes(n)))

main()

#Here are some basic argument specifiers you should know:

#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)

# Exercise 5

# Redo Programming Exercise 2 from Chapter 3. use two functions - one to compute the area of a pizza and one to compute cost per square inch.

#This program will calculate the cost per square inch of a pizza given its diameter and price

#Don't forget you may need float as the divsion may not produce integers (Final output will say 0). When formatting at the end, use %f for floating point numbers

import math

def area(d):
    return math.pi * (0.5 * d)**2

def costPerInch(d, price):
    return float(price) / area(d)

def main():
    print("This program will calculate the area and the cost per square inch of a pizza given its diameter and price")
    diameter = float(input("What is the diameter of the pizza? "))
    cost = float(input("What is the cost of the pizza? "))
    print("The area of the pizza is %f" % (area(diameter)))
    print("The cost per square inch of the pizza is $%f " % (costPerInch(diameter,cost)))

main()

#Exercise 6

#Write a program to calculate the area of a triangle given the length of its 3 sides as parameters. (See programming exercise 9 from Chapter 3) Use your function to 
#augment triangle2.py from this chapter so that it also displays the area of the triangle

import math

def triangle(a, b, c):
    # The bottom 2 calculations are what is needed from C3Ex9 to calulate the area of a triangle
    s = (a + b + c) / 2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return A

def main():
    a, b ,c  = eval(input("Please enter the length of the 3 sides of the triangle separated by a comma: "))
    A = triangle(a, b, c)
    print("The bottom 4 lines show different ways of formatting")
    print("The area of a triangle is", round(A, 2))
    print("The area of a triangle is %d" %(A))
    print (f"The area of a triangle is {A}.")
    print("The area of a triangle is", round(triangle(a, b, c), 2))

main()

# Exercise 7

# Write a function to compute the nth Fibonacci number. Use your function to solve Programming Exercise 16 from Chapter 3

# This program computes the nth Fibonacci number
# Example 0, 1, 2, 3, 4, 5, 6, 7
#         0, 1, 1, 2, 3, 5, 8, 13

def Fibonacci(number):
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return (Fibonacci(number - 2) + Fibonacci(number - 1))

def main():
    number = int(input("Enter the Range Number: "))
    for n in range(0, number):
        print(Fibonacci(n))

main()

# Exercise 8 

# Solve Programming Exercise 17 from Chapter 3 using a function nextGuess(guess, x)
import math
def square_root(x, n):
    guess = x / 2
    
    for i in range(n):
        guess = (guess + x / guess) / 2
    
    return guess
def nextguess(x, guess):
    return (guess + (x / guess)) / 2

def sqrt2(x,n):
    guess = x / 2
    for i in range(n):
        guess = nextguess(x, guess)
    return guess

def main():
    x = float(input("Please enter a number: "))
    n = eval(input("How many times do you want to try?"))

    g = sqrt2(x, n)
    diff = math.sqrt(x) - g
    print("Approximate square root is {0:0.2f},Difference from math.sqrt is {1:0.2f}.".format(g, diff))
main()

# Exercise 9

# Original problem from Chapter 5 Exercise 3
# A certain CS professor gives 100-point exams that are graded on the scale90- 100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
# Write a program that accepts an exam score as input and prints out the corresponding grade.

# New problem
# Do Programming Exercise 3 from Chapter 5 using a function grade (score) that returns the letter grade for a score.
def grade(score):
    if score<60:
        return "F"
    elif score< 70:
        return "D"
    elif score <80:
        return "C"
    elif score <90:
        return "B"
    else:
        return "A"

def main():
    score = int(input("Enter the score:"))
    print("The grade is", grade(score))
main()

# Exercise 10

#Do Programming Exercise 4 from Chapter 5 using a function acronym(phrase) that returns an acronym for a phrase supplied as a string.

# Acronym generator using functions

def acronym(phrase):
    ans = ""
    for word in phrase.split():
        ans = ans + word[0]
    return ans.upper()

def main():
    print("Phrase to Acronym builder")
    words = input("Enter a phrase: ")
    print()
    print("Acronym:", acronym(words))

main()

# Exercise 11

# Write and test a function to meet this specification

# squareEach(nums) is a list of numbers. Modify the list by squaring each entry

import math

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def main():
    nums = list(range(10))
    squareEach(nums)
    print(nums)

main()

# Exercise 12
# Write and test a function to meet this specification
# sumList(nums) nums is a list of numbers. Return the sum of numbers in the list

import math
def sumList(nums):
    sum = 0 # Don't forget here to use 0 as the integer and not "" as I first did thinking I could add to a list
    for i in nums:
        sum = sum + i
    return sum

def main():
    nums = list(range(10))
    print(sumList(nums))

main()

# Exercise 13.
# Write and test a function to meet this specification

# toNumbers(strList) strList is a list of strings each of which represents a number. Modifies each entry in the list by
# converting it to a number

def toNumbers(strList):
    for number in range(len(strList)):
        strList[number] = float(strList[number])

def main():
    list = ["1", "99", "83", "4", "65", "6", "7", "8", "9", "10"]
    toNumbers(list)
    print(list)

main()

# Exercise 14
# Sum of squares from file. I have a file called list.txt which contains numbers 1-10

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def sumList(nums):
    total = 0
    for i in nums:
        total = total + i
    return total

def squareEach(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]**2
    return total
        
def main():
    print("Program to find sum of squares from numbers in a file")
    infile = input("please input a file name:")
    data = open(infile, "r").readlines()
    toNumbers(data)
    squareEach(data)
    print("Sum of squares:", squareEach(data))

main()

# Exercise 15

# This function can draw a smiley or grim face. Demonstrate the function by writing a program that draws several faces of varying sizes in a single window

from graphics import *

def drawFace(center, size, window):
    # head draws a circle centered at a point with a radius of size
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(window)
    # lefteye
    eyeSize = size * 0.25
    eyeOff = size / 2.5
    leftEye = Circle(center, eyeSize)
    # Moving an object move(dx,dy) moves the object dx units in the x direction and dy units in the y direction
    leftEye.move(-eyeOff, -eyeOff)
    leftEye.draw(window)
    # righteye
    rightEye = Circle(center, eyeSize)
    rightEye.move(eyeOff, -eyeOff)
    leftEye.setFill("black")
    rightEye.setFill("black")
    rightEye.draw(window)
    # mouth
    mouthSize = 0.8 * size
    mouthOff = size / 2.0
    p1 = center.clone()
    p1.move(-mouthSize / 2, mouthOff)
    p2 = center.clone()
    p2.move(mouthSize / 2, mouthOff)
    mouth = Line(p1, p2)
    mouth.draw(window)

def main():
    win = GraphWin("Faces")
    drawFace(Point(50, 50), 20, win)
    drawFace(Point(100, 100), 30, win)
    drawFace(Point(160, 160), 40, win)
    win.getMouse()
    win.close()

main()

# Exercise 16
# Overlaying a face on a photo or gif

from graphics import *

def drawFace(center, size, window):
    eyeSize = 0.15 * size
    eyeOff = size / 3.0
    mouthSize = 0.8 * size
    mouthOff = size / 2.0
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(window)
    leftEye = Circle(center, eyeSize)
    leftEye.move(-eyeOff, -eyeOff)
    rightEye = Circle(center, eyeSize)
    rightEye.move(eyeOff, -eyeOff)
    leftEye.draw(window)
    rightEye.draw(window)
    leftEye.setFill("black")
    rightEye.setFill("black")
    p1 = center.clone()
    p1.move(-mouthSize/2, mouthOff)
    p2 = center.clone()
    p2.move(mouthSize/2, mouthOff)
    mouth = Line(p1,p2)
    mouth.draw(window)

def interactiveFace(w):
    center = w.getMouse()
    edge = w.getMouse()
    radius = distance(center, edge)
    drawFace(center, radius, w)

def distance(p1, p2):
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    return (dx*dx + dy*dy)**.5

def createPicWin(picFile):
    img = Image(Point(0,0),picFile)
    width = img.getWidth()
    height = img.getHeight()
    win = GraphWin(picFile, width, height)
    img.move(width//2, height//2)
    img.draw(win)
    return win

def main():
    print("Photo Anonymizer: Draw faces over pictures.")
    picFile = input("Enter name of file containing GIF image: ")
    win = createPicWin(picFile)
    numFaces = int(input("How many faces to draw? "))
    for i in range(numFaces):
        print("Click center and edge of a face.")
        interactiveFace(win)
    print("Click again to quit.")
    win.getMouse()
    win.close()
    
main()

# Chapter 6 - Exercise 17
# Moving a circle with a function

from graphics import *

def moveTo(shape, newCenter):
    center = shape.getCenter() # returns a clone of the center point of the circle
    dx = newCenter.getX() - center.getX() # Returns the x value of a point
    dy = newCenter.getY() - center.getY() # Returns the y value of a point
    shape.move(dx,dy)

def main():
    win = GraphWin("Circle Mover", 400, 400) # GraphWin(title, width, height)
    item = Circle(Point(200,200), 40) # Constructs a circle with a given center point and radius)
    item.setFill("red") # Fill circle in chosen colour
    item.draw(win) # Draw the circle
    for i in range(10): # For range of 10 clicks
        p = win.getMouse() # Pauses for the user to click the mouse in the window and returns p as the point where the mouse was clicked
        moveTo(item, p) # Go to the moveTo function
    win.getMouse()
    win.close() # Closes the on screen window

main()
