# Review Questions 
# True/False 
# 1. A Python string literal is always enclosed in double quotes. False 
# A1. Reference Page 130 "A string literal is formed by enclosing some characters in quotation marks. Python also allows strings to be delineated by single quotes
#     (apostrophes).There is no difference; just be sure to use a matching set."
#
# 2. The last character of a strings is at position len(s) -1. True s[-1]
# A2. Reference Page 131 "Notice that in a string of n characters, the last character is at position n -1, because the index starts at 0." Length will give the length 
#     of a string and the n-1 value of the len will always be the last character
##
# 3. A string always contains a single line of text. False
# A3. Reference Page 131. A string is a sequence of characters. This sequence can be of any length. In fact, it is also possible to have an empty string, i.e. "".]
#
# 4. In Python "4" + "5" is "45". True string format
# A4. Reference Page 132. Handy operators for string concatenation is (+) which builds a string by glueing two strings together
#
# 5. Python lists are mutable, but strings are not. True
# A5. Reference Page 138. "While strings and lists are both sequences, there is an important difference between the two. Lists are mutable. That means that the value
#     of an item in a list can be modified with an assignment statement. Strings, on the other hand, cannot be changed 'in place'"
#
# 6. ASCII is a standard for representing characters using numeric codes. True and Unicode
# A6. Reference Page 140. "One important standard is called ASCII (American Standard Code for Information Interchange).ASCII uses the numbers 0 through 127 to represent
#     characters typically found on an (American) computer keyboard, as well as certain special values known as control codes that are used to coordinate the sending and
#     receiving of information.
#
# 7. The split method breaks a string into a list of substrings, and join does the opposite. Falsex True 
# A7. Reference Page 144 "Strings have built in methods The split method splits a string into a list of substrings. By default, it will split the string whever a space
#     occurs. Information on string methods can be seen in the table on Page 148.
#
# Q8. A substitution cipher is a good way to keep sensitive information secure. FALSE
# A8. Reference Page 150 "Substitution ciphers are a weak form of encryption. Since each letter is always encoded by the same symbol, a codebreaker coud use statistical
#     information about the frequency of various letters and some simple trial and error testing to discover the original message."
#
# Q9. The add method can be used to add an item to the end of a list. FALSE
# A9. Reference Page 147 "The append method can be used to add an item at the end of a list. This is often used to build a list an item at a time."
#
# Q10. The process of associating a file with an object in a program is called "reading" the file. FALSE
# A10. Reference Page 159 "We need some way to associate a file on disk with an object in a program. This process is called opening a file. Once a file has been opened, its 
#      contents can be accessed through the associated file object.
Multiple Choice 
#     1. Accessing a single character out of a string is called: ax [d]
#     a) slicing b) concatenation c) assignment d) indexing 
# 
#     2. Which of the following is the same ass [0 : -1] ? c
#     a) s [-1] b) s [ :] c) s [ : len(s) -1] d) s [O : len(s)] 
# 
#     3. What function gives the Unicode value of a character? a
#     a) ord b) ascii c) chr d) eval 
#     Reference Page 140. "Python provides a couple of built-in functions that allow us to switch back and forth between characters and the numberic values used to represent 
#     them in strings. The ord function returns the numeric ("ordinal") code of a single-character string, while chr goes the other direction."
#
#     4. Which of the following can not be used to convert a string of digits into a number? c
#     a) int b) float c) str d) eval 
#
#     5. A successor to ASCII that includes characters from (nearly) all written languages is c
#     a) TELLI b) ASCII++ c) Unicode d) ISO
#     Reference Page 140. "Most modern systems are moving to Unicode, a much larger standard that aims to include the characters of nearly all written languages."
#
#     6. Which string method converts all the characters of a string to upper case? d Page 148 table
#     a) capitalize b) capwords c) uppercase d) upper 
#
#     7. The string "slots" that are filled in by the format method are marked by: d
#     a) % b) $ c) [] d) {} 
#     Reference Page 156. "Curly braces ({}) inside the template-string mark 'slots' into which the provided values are inserted. The information inside the curly braces
#     tells which value goes in the slot and how the value should be formatted.
#
#     8. Which of the following is not a file-reading method in Python? c Reference Page 161. 
#     a) read b) readline c) readall d) readlines 
#     
#     9. The term for a program that does its input and output with files is c
#     a) file-oriented b) multi-line c) batch d) lame 
#
#     10. Before reading or writing to a file, a file object must be created via a
#     a) open b) create c) File d) Folder

# Q1. Given the initial statements, show the results of evaluating each of the following string expressions
#
#     s1 = "spam"
#     s2 = "ni!"
#
#                                      |  Expected answer
#     Q1a "The knights who say, " + s2 |  The knights who say, ni!
#
#     Q1b. 3 * s1 + 2 * s2             |  spamspamspamni!ni!
#
#     Q1c. s1[1]                       |  p
#
#     Q1d. s1[1:3]                     |  pa
#
#
#     Q1e. s1[2] + s2[:2]              |  ani
#
#     Q1f. s1 + s2[-1]                 |  spam!
#
#     Q1g. s1.upper()                  |  SPAM
#
#     Q1h. s2.upper().ljust(4) * 3     |    NI! NI! NI! 
#     Page 148 for table of string methods
#
# Q2. Given the same initial statements as in the previous problem, show a Python expression that could construct each of the following results by performing string 
#     operations on s1 and s2
#
#     s1 = "spam"
#     s2 = "ni!"
#                                         |  Expected answer
#    a) "NI"                              |  s[:2].upper()
#    b) "ni!spamni!"                      |  s2 + s1+ s2
#    c) "Spam Ni! Spam Ni! Spam Ni!"      |  (s1.capitalize() + " " +s2.capitalize()) *3 
#    d) "spam"                            |  s1
#    e) ["sp" , "m"]                      |  s1.split('a')
#    f) "spm"                             |  s[:2]+ s[-1]
#
#
# Q3. Show the output of that would be generated by each of the following program fragments
# 
#                                         |  Expected answer
# Q3a. for ch in "aardvark":
            prin(ch)
                                          |  a
                                             a
                                             r
                                             d
                                             v
                                             a
                                             r
                                             k

         
# 
#
# Q3b. for w in "Now is the winter of our discontent...".split():
           print(w)
Now
is
the
winter
of
our
discontent
...
#
# Q3c for w in "Mississippi".split("i"):
  print(w, end=" ")
# A:M ss ss pp
#
# Q3d
msg = ""
for s in "secret".split("e"):
  msg = msg + s
print(msg)
# Ad: scrt
#
# Q3e
msg = ""
for ch in "secret":
  msg = msg + chr(ord(ch)+1)
 print(msg)
 # Ae: tfdsfu
 #
 #
# Q4. Show the string that would result from each of the following string formatting operations. If the operation is not legal, explain why:
#
#     a) "Looks like {1} and {0} for breakfast".format("eggs", "spam")
#         'Looks like spam and eggs for breakfast'
#        The operation is not legal. Curly braces are required around 1 and 0.

#     b) "There is {0} {1} {2} {3}".format(1, "spam", 4 "you")
#         'There is 1 spam 4 you.'

#     c) "Hello {0}".format("Susan", "Computewell")
#        'Hello Susan'

#     d) "{0:0.2f} {0:0.2f}".format(2.3, 2.3468)
#        '2.30 2.30'

#     e) "{7.5f} {7.5f}".format(2.3, 2.3468)
#        The operation is not legal. There is no index followed by : supplied in each of the curly braces.
#        Replacement index 7 out of range for positional args tuple

#     f) "Time left {0:02}:{1:05.2f}".format(1, 37.374)
#        'Time left 1:37.37'

#     g) "{1:3}".format("14")
#        The operation is not legal. There is only one index, no second index is supplied in the list.
#       Replacement index 1 out of range for positional args tuple
#
#
# Q5. Explain why public key encryption is more useful for securing commmunications on the Internet than private (shared) key encryption.
#
#     Private keys must be known by both parties ahead of time. When contacting sites on the internet, say for e-commerce, there would be no practical way for the parties
#     to exchange the private key.Only the party holding the decryption key will be able to decipher it.
#
# Programming Exercises
#
# Q1. As discussed in the chapter, string formatting could be used to simplify the dateconvert2 . py program. Go back and redo this program making use of the 
#      string-formatting method.
#
# dateconvert2.py
# Converts day month and year numbers into two date formats
def main() : 
    # get the date 
    dateStr = input ( "Enter a date (mm/dd/yyyy) : ") 
    # split into components 
    monthStr, dayStr, yearStr = dateStr.split("/") 
    # convert monthStr to the month name 
    months = ["January", "February", "March" , "April", "May", "June", "July"
    "August", "September", "October", "November", "December"]
    monthStr = months[int(monthStr) -1] 
    # output result in month day , year format  
    print ("The converted date is : {0} {1},{2}.".format(monthStr, dayStr, yearStr))
    
main()
#
#
# Q2. A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an input and
#      prints out the corresponding grade.
#
#
# Quiz grader

def main():
    print("Five point quiz grader")
    score = int(input("Enter the score: "))
    grade = "FFDCBA"[score]
    print("The grade is", grade)

main()
#
# Q3. A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#     Write a program that accepts an exam score as input and prints out the corresponding grade.
#
# c05ex03.py
# Exam grader
def main():
    print("Exam Grader")
    score = int(input("Enter the score (out of 100): "))
    grades = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    print(grades)
    print("The grade is", grades[score])

main()
#
# Q4. An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For example, RAM is an acronym for "random access memory." 
#     Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase. Note: The acronym should be all uppercase, even if the words
#     in the phrase are not capitalized.
#
#acronym.py
def main():
    print("acronym.py")
    phrase = input("Enter the phrase you want an acronym for:")
    acronym = ""
    
    for w in phrase.split():
        acronym = acronym + w[0].upper()
    print("The acronym is", acronym)
    
main()
#
# Q5. Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name. The value of a name is determined by summing up
#     the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3, up to "z" being 26. For example, the name "Zelle" would have the value  26 + 5 +12
#      + 12 + 5 = 60 (which happens to be a very auspicious number, by the way). Write a program that calculates the numeric value of a single name provided as input.
#      
#
#numeric value.py
# using unicode
def main():
    print("numeric value.py")
    name = str(input("Please enter you name:"))
    name = name.lower()
    value = 0
    for ch in name:
        numeric = ord(ch)- 96
        value = value + numeric
        print(ch, numeric)
    print("The numeric value of your name is", value)
        
main()

#using indexing
def main():
    #
    name = input("Enter your name:").lower()
    letters = " abcdefghijklmnopqrstuvwxyz"
    value = 0
    
    for ch in name:
        index = letters.find(ch)
        print(ch, index)
        value = value + index
    print("The numeric value of your name is", value)
    
main()
#
#
# Question 6.Expand your solution to the previous problem to allow the calculation of a complete name such as "John Marvin Zelle" or "John Jacob Jingleheimer Smith." The 
# total value is just the sum of the numberic values of all the names.
#
# fullname.py
# Numerology of a full name
def main():
    #
    name = input("Enter your name:").lower()
    full = "".join(name.split())
    
    letters = " abcdefghijklmnopqrstuvwxyz"
    value = 0
    
    for ch in full:
        index = letters.find(ch)
        print(ch, index)
        value = value + index
    print("The numeric value of your name is", value)
    
main()
#
#
# Q7. A Caesar cipher is a simple substitution sipher based on the idea of shifting each letter of the plaintext message a fixed number (called the key) of positions in
#     the alphabet. For example, if the key is 2, the word "Sourpuss" would be encoded as "Uqwtrwuu." The original message can be recovered by "reencoding" it using the 
#     negative of the key.
#
#     Write a program that can enconde and decode Caesar ciphers. The input to the program will be a string of plaintext and the value of the key. The output will be an
#     encoded message where each character in the original message is replaced by shifting it key characters in the Unicode character set. For example, if ch is a 
#     character in the  string and key is the amount to shift, then the character that replaces ch can be calculated as: chr(ord(ch) + key)
#
#cipher.py
def main():
    plaintext = input("Please input the message you want to encode:")
    key = int(input("Enter the key:"))
    cipher = ""
    for ch in plaintext:
        index= ord(ch) + key
        cipher = cipher + chr(index)
    print(cipher)
    
main()     
#
# Q8. One problem with the previous exercise is that it does not deal with the case when we "drop off the end" of the alphabet. A true Caesar cipher does the shifting
#     in a circular fashion where the next character after "z" is "a." Modify your solution to the previous problem to make it circular. You may assume that the input 
#     consists only of letters and spaces.
#     Hint: Make a string containing all the characters of your alphabet and use positions in this string as your code. You do not have to shift "z" int "a"; just make
#     sure that you use a circular shift over the entire sequence of characters in your alphabet string.
#
#cipher2.py
def main():
    plaintext = input("Please input the message you want to encode:")
    key = int(input("Enter the key:"))
    key = key % 26
    cipher = ""
    for ch in plaintext:
        
        if  ch >= 'a' and ch <='z' :
            index= ord(ch) + key
            if index > 122:
                index = index - 24
            else:
                index= ord(ch) + key
        elif ch >= 'A' and ch <='Z' :
            index= ord(ch) + key
            if index >ord('Z'):
                index = index -24
        else:
            index = ord(ch)
        
        cipher = cipher + chr(index)
    print(cipher)
    
main()
#
# Q9. Write a program that counts the number of words in a sentence entered by the user.
#
def main():
    sentence = str(input("Please enter your sentence here: "))
    #Example: I shot the sheriff
    words = sentence.split() 
    # example: ['I', 'shot', 'the', 'sheriff']
    print(words) # Put this in to see the output of splitting the sentence
    number = len(words)
    print("The number of words in the sentence,", sentence, "is", number)
main()
#
# Q10. Write a program that calculates the average word length in a sentence entered by the user.
#      Same as above, but also count length of each words, add up all the numbers, divide by number of words.
#
# Averge.py
# Get the average word count from an input phrase or sentence
#average.py
def main():
    sentence = str(input("Please enter your sentence here: "))
    #Example: I shot the sheriff
    words = sentence.split() 
    # example: ['I', 'shot', 'the', 'sheriff']
    print(words) # Put this in to see the output of splitting the sentence
    total = 0
    for w in words:
        total = total +len(w)
    number = len(words)
    aver = total / number
    print("The average length of words in the sentenceb is", aver)
    
main()
#
# Q11. Write an improved version of the chaos.py program from Chapter 1 that allows a user to input two initial values and the number of of iterations, and then prints
#      a nicely formatted table showing how the values change over time. For example, if the starting values were .25 and .26 with 10 iterations, the table might look 
#      like this:
#
#     index    0.25         0.26
#     ----------------------------
#       1    0.731250     0.750360
#       2    0.766441     0.730547
#       3    0.698135     0.767707
#       4    0.821896     0.695499
#       5    0.570894     0.825942
#       6    0.955399     0.560671
#       7    0.166187     0.960644
#       8    0.540418     0.147447
#       9    0.968629     0.490255
#      10    0.118509     0.974630
#
# File: chaos11. py 
# A simple program illustrating chaotic behavior. 
def main():
    print("This program illustrates a chaotic function") 
    x, y = eval(input("Enter two numbers between 0 and 1(seperated with ","): ")) 
    n = int(input("Please input the iterations times: "))
    
    print(" index     ",x,"         ",y)
    print("-------------------------------")
    for i in range(1,n+1): 
        x = 3.9 * x * (1 - x) 
        y = 3.9 * y * (1 - y)
        print("{0:4}  {1:12.6f}  {2:12.6f}".format(i, x, y))
main()
#
# Q12. Write an improved version of the futval.py program from Chapter 2.
#      Your program will prompt the user for the amount of the investment, the annualized interest rate, and the number of years of the investment. The program will then output a
#      nicely formatted table that tracks the value of the investment year by year. Your output might look something like this:
#
#     Year     Value
#     ----------------
#       0     $2000.00
#       1     $2200.00
#       2     $2420.00
#       3     $2662.00
#       4     $2928.20
#       5     $3221.02
#       6     $3542.12
#       7     $3897.43
#
# c05ex12-futval12.py
# Future value with formatted table.
#
#fvalue.py
def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    years = int(input("Enter the number of years: "))

    print(" Year   Value")
    print("----------------")
    for i in range(years + 1):
        print("{0:3}    ${1:7.2f}".format(i,principal))
        principal = principal * (1 + apr)

main()
#
# Q13. Redo any of the previous programming exercises to make them batch-oriented (using text files for input and output
#
# c05ex13.py
# Batch Caesar cipher
# Input file format: first line is key value; remaining lines are text to encode.

def main():
    print("Batch Caesar cipher")
    print()

    inName = input("Enter name of the input file: ")
    infile = open(inName,'r')
    key = int(infile.readline())

    outName = input("Enter name of output file: ")
    outfile = open(outName, 'w')
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    for line in infile:
        for letter in line[:-1]:
            pos = chars.find(letter)
            newpos = (pos + key) % len(chars)
            print(chars[newpos], file=outfile, end="")
        print(file=outfile)

    infile.close()
    outfile.close()
    print("Done")

main()
#
# Q15. Write a program to plot a horizontal bar chart of student exam scores. Your program should get input from a file. The first line of the file contains the count of the 
#      number of students in the file, and each subsequent line contains a student's last name followed by a score in the range 0-100. Your program should draw a horizontal 
#      rectangle for each student where the length of the bar represents the student's score. The bars should all line up on their left-hand edges.
#
#      Note: Page 158 for File Processing help
#
#      Hint: Use the number of students to determine the size of the window and its coordinates. 
#      Bonus: label the bars at the left with the students' names.
#
# exams_score.py
# exams_score.py
import matplotlib.pyplot as plt # Import the matplot library to plot bar graph
# import dialog box for opening file
#from tkinter.filedialog import askopenfilename 

# intialize the x and y with empty array
x=[]
y=[]

# open the file in read mode
#infilename = askopenfilename() # get the file name
inName = input("Enter name of the input file: ")
grades = open(inName, "r") # open and read file
n_students = grades.readline() # By running this first, we take into account the 5 at the top of the grades.txt input file
print(n_students)

lines = grades.readlines() # read all the lines and store in form of array in Lines variable
 
for line in lines:
    # in each iteration, split line into first name, last name and score
    data=line.strip().split()
    print(data)
    
    x.append(int(data[-1]))# then append the score to x array 
    y.append(data[0])# and append the concatenation of last name


fig, ax = plt.subplots()    # store subplots in fig, and ax

p1=ax.barh(y, x,0.5)  # plot the horizontal bar graph using barh function
ax.bar_label(p1,x, label_type='center')     #label the each bar graph with score using bar label function
plt.ylabel("Students")      # setting label of y-axis
plt.xlabel("Scale of grades ( 0 - 100 )")   # setting label of x-axis   
plt.title("Student Surnames and Grades")    # setting label of title

plt.show()  # At last, this command helps to show plot
#
#
# Q16. Write a program to draw a quiz score histogram. Your program should read data from a file. Each line of the file contains a number in the range 0-10. Your program must 
#      count the number of occurences of each score and then draw a vertical bar chart with a bar for each possible score (0-10) with height corresponding to the count of that 
#      score. For example, if 15 students got an 8, then the the height of the bar for 8 should be 15.
#      Hint: Use a list that stores the count for each possible score.
#
# quiz score histogram
import matplotlib.pyplot as plt # Import the matplot library to plot bar graph
# import dialog box for opening file
#from tkinter.filedialog import askopenfilename 

# open the file in read mode
#infilename = askopenfilename() # get the file name
inName = input("Enter name of the input file: ")
quizscores = open(inName, "r") # open and read file

counts = []
scores = quizscores.readlines()  # Read all the lines in the file and store it in a list

for i in range(11):
    counts.append(scores.count(str(i)+"\n"))
    
plt.bar(range(11),counts,align='center')

plt.gca().set_xticks(range(11))
plt.show()
#
#
#

