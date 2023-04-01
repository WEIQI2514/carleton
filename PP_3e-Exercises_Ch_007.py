# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 7: Decision Structures
# End-of-Chapter Exercises
#
# REVIEW QUESTIONS
#
# True/False
# 1. A simple decision can be implemented with an if statement. True

# 2. In Python conditions, /= is written as/=.  False !=

# 3. Strings are compared by lexicographic ordering. True

# 4. A two-way decision is implemented using an if-elif statement. True

# 5. The math.sqrt function cannot compute the square root of a negative number. True

# 6. A single try statement can catch multiple kinds of errors. False reference page??

# 7. Multi-way decisions must be handled by nesting multiple if-else statements. False
# Reference page 222:There is another way to write multi-way decisions in Python that preserves the semantics of the nested structures but gives it a more appealing 
# look. The  idea is to combine an el se followed immediately by an if into a single clause  called an el if (pronounced "ell-if").

# 8. There is usually only one correct solution to a problem involving decision structures. False
# Reference page 234:There is more than one way to do it. 

# 9. The condition x <= y <= z is allowed in Python. True
# Reference page 228:The condition x1 >= x2 >= x3 does not match the template for conditions shown above. Most computer languages would not accept this as a valid 
# expression. It turns out that Python does allow this compound condition, and it behaves exactly like the mathematical relations xl >= x2 >= x3.

# 10. Input validation means prompting a user when input is required. False
# Reference page 262: If the user types an incorrect input, the pro gram asks for another value. It continues to reprompt until the user enters a valid value. This 
# process is called input validation.
#
# 
# Multiple Choice
# 1. A statement that controls the execution of other statements is called a c)
# a) boss structure b) super structure c) control structure* d) branch 

# 2. The best structure for implementing a multi-way decision in Python is c)
# a) if b) if- else c) if- elif- else* d) try 

# 3. An expression that evaluates to either true or false is called b)
# a) operational b) Boolean* c) simple d) compound

# 4. When a program is being run directly (not imported), the value of __name __ IS b)
# a) script b) main* c) __main__ d) True 

# 5. The literals for type bool are b)
# a) T, F b) True, False* c) true, false d) 1, 0 

# 6. Placing a decision inside of another decision is an example of c)
# a) cloning b) spooning c) nesting* d) procrastination 

# 7. In Python, the body of a decision is indicated by a)
# a) indentation* b) parentheses c) curly braces d) a colon 

# 8. A structure in which one decision leads to another set of decisions, which leads to another set of decisions, etc., is called a decision tree
# a) network b) web c) tree* d) trap 

# 9. Taking the square root of a negative value with math.sqrt produces a(n) a)
# a) ValueError* b) imaginary number c) program crash d) stomachache 

# 10. A multiple choice question is most similar to c）
# a) simple decision b) two-way decision c) multi-way decisions* d) an exception handler 
#
# Discussion
#
# 1.  Explain the following patterns in your own words: 
#   a) simple decision：when the condition is true, The sequence of statements are executed, if it is false, skip the statements. 
#     Answer：  The sequences of statements in a simple decision excecutes when the condition true. If it is false, the statements are skipped.
#   b) two-way decision 
#     Answer：  A two-way decision is a simple decision with two parts. If the condition is true, the statements are executed. If it is false, a different set of  statements is excecuted.
#   c) multi-way decision 
#    Answer： Multi-way decisions specifiy different conditions, which, if true, lead to different sets of statements being executd.
#     
# 2.  How is exception handling using try/except similar to and different from handling exceptional cases using ordinary decision structures (variations on if)?
#  
#   Answer：Exception-handling is conditional, similar to if statements. If an error occurs in the body of the try statement, Python looks for an except clause with a
#   matching error and excecute the handler code if an appropriate except is found.
#
# 3. The following is a (silly) decision structure:
a, b, c = eval( input('Enter three numbers : '))
if a > b: 
    if b > c: 
        print("Spam Please!" ) 
    else : 
        print("It's a late parrot!" ) 
elif b > c: 
    print("Cheese Shoppe" ) 
    if a >= c: 
        print("Chedda r" ) 
    elif a < b: 
        print ("Gouda") 
    elif c == b: 
        print("Swiss") 
else: 
    print("Trees") 
    if a == b: 
        print("Chestnut" ) 
    else : 
        print ("Larch") 
print ("Done" )

# Show the utput that would result from each of the following possible inputs: 
#              |Expecting result
a) 3, 4, 5     Trees\n  Larch\n Done              
b) 3, 3, 3     Trees\n Chestnut\n Done
c) 5, 4, 3     Spam Please!\n Done
d) 3, 5, 2     Cheese Shoppe\n Cheddar\n Done
e) 5, 4, 7     It's a late parrot!\n Done
f) 3, 3, 2     Cheese Shoppe\nCheddar\n Done
#    
# 1. Many companies pay time-and-a-half for any hours worked above 40 in a given week. Write a program to input the number of hours worked and the hourly rate and
#     calculate the total wages for the week. 
def wage(hour,rate):
    if hour > 40:
        wage = hour*rate +(hour-40) * 1.5 *rate
    else:
        wage = hour *rate
    return wage

def main():
    hour = int(input("How many hours have you worked?"))
    rate = float(input("Please enter the hourly rate"))
    ans = wage(hour, rate)
    print("Your monthly wage is:",ans)
    
main()
# from others
def main():
    print("Weekly pay calculator \n")
    hours = float(input("Enter hours worked: "))
    rate = float(input("hourly wage: "))
    if hours <= 40:
        pay = hours * wage
    else:
        pay = 40 * wage + (hours-40) * 1.5 * wage

    print("Your week's pay is ${0:0.2f}.".format(pay))

if __name__ == '__main__':
    main()

# 2. A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an input
#    and uses a decision structure to calculate the corresponding grade.
def main():
    try:
        score = int(input('Enter quiz score: '))
        if score == 5:
            print('Grade of the score: A')
        elif score == 4:
            print('Grade of the score: B')
        elif score == 3:
            print('Grade of the score: C')
        elif score == 2:
            print('Grade of the score: D')
        else:
            print('Grade of the score: F')
    except:
        print('Enter a valid score, integer from 0 to 5')

main()

# 3. A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:0, <60:F. Write a program that accepts an exam score 
# as input and uses a decision structure to calculate the corresponding grade.
def main():
    print("Exam grade calculator \n")
    try:
        score = int(input('Enter quiz score: '))
        if 90 <= score <= 100:
            print('Grade of the score: A')
        elif score >= 80:
            print('Grade of the score: B')
        elif score >= 70:
            print('Grade of the score: C')
        elif score >= 60:
            print('Grade of the score: D')
        elif 0 <= score < 60:
            print('Grade of the score: F')
        else:
            print('Enter a valid score from 0 to 100')    
    except:
        print('Wrong input! Enter a valid score from 0 to 100')

main()
# c07ex3.py
#  exam grade

def main():
    print("Exam grade calculator \n")
    score = int(input("Enter exam score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        
    print("The grade is ", grade,".")

if __name__ == '__main__':
    main()
    
# 4. A certain college classifies students according to credits earned. A student with less than 7 credits is a Freshman. At least 7 credits are required to be 
# a Sophomore, 16 to be a Junior and 26 to be classified as a Senior. Write a program that calculates class standing from the number of credits earned.
#Q4 student credit
def main():
    print("Class standing calculator\n")
    earned_credits = float(input("how many creadits have you earned?"))
    
    if earned_credits < 7:
        student_type = 'Freshman'
    elif earned_credits <= 16:
        student_type = 'Sophomore'
    elif earned_credits <= 26:
        student_type = 'Junior'
    else:
        student_type = 'Senior'
        
    print('You are a',student_type, 'student!')
    
main()

# 5. The body mass index (BMI) is calculated as a person's weight (in pounds) times 720, divided by the square of the person's height (in inches). A BMI in the range
#    19-25, inclusive, is considered healthy. Write a program that calculates a person's BMI and prints a message telling whether they are above, within, or below the
#    healthy range.
#Q5
def main():
    print("BMI calculator \n")
    weight = float(input('Enter weight in pounds: '))
    height = float(input('Enter height in inches: '))
    bmi = (weight * 720) / height**2
    if bmi < 19:
        print('Bellow the healthy range!')
    elif bmi > 25:
        print('Above the healthy range!')
    else:
        print('Within the healthy range!')

main()

# c07ex5.py
#    body mass index

def main():
    
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))
    bmi = weight * 720 / height**2
    print = ("Your BMI is ", bmi,".")
    if bmi < 19:
        print("You are below the healthy range.")
    elif bmi <= 25:
        print("You are in the healthy range.")
    else:
        print("You are above the healthy range.")

if __name__ == '__main__':
    main()
    
# 6. The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a penalty of $200 for any speed over 90 mph. Write a program 
# that accepts a speed limit and a clocked speed and either prints a message indicating the speed was legal or prints the amount of the fine, if the speed is illegal.
#Q6 speedlimit
def main():
    sLimit = int(input('Enter speed limit: '))
    clockedSpeed = float(input('Enter clocked speed: '))
    dSpeed = clockedSpeed - sLimit
    if dSpeed <= 0:
        print('Legal speed')
    else:
        if clockedSpeed <= 90:
            fine = 50 + (dSpeed*5)
            print('Fine:', fine)
        else:
            fine = 50 + (90 - sLimit) * 5 + 200
            print('Fine:', fine)

main()

# c07ex6.py
#    speeding fine

def main():
    print("Speeding fine calculator \n")
    speedlimit = int(input("Enter speed limit: "))
    clockedspeed = int(input("Enter clocked speed: "))
    if clockedspeed <= speedlimit:
        print("The speed is legal.")
    else:
        print("The speed is illegal.")
        if clockedspeed > 90:
            fine = 5 * (clockedspeed - speedlimit) + 50 + 200
        else:
            fine = 5 * (clockedspeed - speedlimit) + 50
        print("The fine is ${0:02f}.".format(fine))

if __name__ == '__main__':
    main()
    
# 7. A babysitter charges $2.50 an hour until 9:00 PM when the rate drops to $1.75 an hour (the children are in bed). Write a program that accepts a starting time and
#  ending time in hours and minutes and calculates the total babysitting bill. You may assume that the starting and ending times are in a single 24-hour period. 
#  Partial hours should be appropriately prorated.


# 8. A person is eligible to be a US senator if they are at least 30 years old and have been a US citizen for at least 9 years. To be a US representative these numbers
#  are 25 and 7, respectively. Write a program that accepts a person's age and years of citizenship as input and outputs their eligibility for the Senate and House.

# 9. A formula for computing Easter in the years 1982-2048, inclusive, is as follows: let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30, e = (2b + 4c + 6d + 5)%7.
#  The date of Easter is March 22 + d + e (which could be in April). Write a program that inputs a year, verifies that it is in the proper range, and then prints out 
#  the date of Easter that year.

# 10. The formula for Easter in the previous problem works for every year in the range 1900-2099 except for 1954, 1981, 2049, and 2076. For these 4 years it produces a
#     date that is one week too late. Modify the above program to work for the entire range 1900-2099.

# 11. A year is a leap year if it is divisible by 4, unless it is a century year that is not divisible by 400. (1800 and 1900 are not leap years while 1600 and 2000 are.)
#     Write a program that calculates whether a year is a leap year.

# 12. Write a program that accepts a date in the form month! day /year and outputs whether or not the date is valid. For example 5/24/1962 is valid, but 9/31/2000 is not.
# (September has only 30 days.)

# 13. The days of the year are often numbered from 1 through 365 (or 366). 
# This number can be computed in three steps using int arithmetic: 
# (a) dayNum = 31(month - 1) +day 
# (b) if the month is after February subtract (4(month) + 23)/ /10 
# (c) if it's a leap year and after February 29, add 1 
# Write a program that accepts a date as month/ day /year, verifies that it is a valid date (see previous problem), and then calculates the corresponding day number.

# 14. Do Programming Exercise 7 from Chapter 4, but add a decision to handle the case where the line does not intersect the circle.


# 15. Do Programming Exercise 8 from Chapter 4, but add a decision to prevent the program from dividing by zero if the line is vertical.


# 16. Archery Scorer. Write a program that draws an archery target (see Programming Exercise 2 from Chapter 4) and allows the user to click five times to represent
# arrows shot at the target. Using five-band scoring, a bulls-eye (yellow) is worth 9 points and each successive ring is worth 2 fewer points down to 1 for white. The 
# program should output a score for each click and keep track of a running sum for the entire series.

# 17. Write a program to animate a circle bouncing around a window. The basic idea is to start the circle somewhere in the interior of the window. Use variables dx and dy
# (both initialized to 1) to control the movement of the circle. Use a large counted loop (say 10000 iterations), and each time through the loop move the circle using 
# dx and dy . When the x-value of the center of the circle gets too high (it hits the edge), change dx to -1. When it gets too low, change dx back to 1. Use a similar 
# approach for dy . Note: Your animation will probably run too fast. You can slow it down by using update from the graphics library with a rate parameters. For example,
# this loop will be limited to going around at a rate of 30 times per second: 
 for i in range ( 10000) : 
    ...
    update (30) # pause so rate is not more than 30 times a second

# 18. Take a favorite programming problem from a previous chapter and add decisions and/ or exception handling as required to make it truly robust (will not crash on
#   any inputs). Trade your program with a friend and have a contest to see who can ''break" the other's program.













