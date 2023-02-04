### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
### Chapter 2: Writing Simple Programs
### 2.9 Exercises

### Review Questions 

##True/False 

# 1. The best way to write a program is to immediately type in some code and then debug it until it works. F
#     [Explanation: p.27-8 "Writing large programs is daunting challenge. It would be almost impossible without a systematic approach. 
#	  The process of creating a program is often broken down into stages according to the information that is produced in each phase."
#     p. 29 "Susan knows better than to just dive in and start writing a program without first having a clear idea of what to build."]
#
# 2. An algorithm can be written without using a programming language. T
#     [Explanation: p.30 "Susan could write her algorithm down in a computer language. However,the precision required to write it out 
#	  formally tends to stifle the creative process of developing the algorithm. Instead, she writes her algorithm using pseudocode. 
#     Pseudocode is just precise English that describes what a program does. It is meant to communicate without all the extra mental 
#     overhead getting the details right in any particular programming language."]
#
# 3. Programs no longer require modification after they are written and debugged. F
#     [Explanation: see step called "Maintaining the Program' on p.28: "Continue developing the
#     program in response to the needs of your users. Most programs are never really finished;
#     they kepp evolving over years of use."]
# 4. Python identifiers must start with a letter or underscore. T
#     [Explanation: p.31 "Python has rules about how identifiers are formed. Every identifier must
#     begin with a letter or underscore (the "_" character) which may be followed by any sequence
#     of letters, digits, or underscores. This implies that a single identifier cannot contain any
#     spaces."]
# 5. Keywords make good variable names. F
#     [Explanation: p.31 "One important thing to be aware of is that some identifiers are part of
#     Python itself. These names are called reserved words or keywords and cannot be used as ordinary
#     identifiers."]

# 6. Expressions are built from literals, variables, and operators.T
#     [Explanation: p.32: "The simplest kind of expression is a literal." p.33 "A simple identifier
#     can also be an expression. We use identifiers as variables to give names to values. When an
#     identifier appears as an expression, its value is retrieved to provide a result for the
#     expression. p.34 "More complex and interesting expressions can be constructed by combining
#     simpler expressions with operators."]

# 7. In Python, x = x + 1 is a legal statement. T
#     [Explanation: p.37 "Sometimes it's helpful to think of a variable as a sort of named storage
#     location in computer memory, a box that we can put a value in. When the variable changes, the old
#     value is erased and a new one written in. Figure 2.1 shows how we might picture the effect of
#     x = x + 1 using this model. This is exactly the way assignment works in some computer languages.
#     It's also a very simple way to view the effect of assignment, and you'll find pictures similar to
#     this throughout the book."]
#     [Interesting aote: In a functional programming language (e.g., Racket), this would be illegal.]
# 8. Python does not allow the input of multiple values with a single statement. F
#     [Explanaion: drawn from p. 41 on simultaneous assignment and p. 39 on input: Since Python allows
#     simultaneous assignment, the built-in input function can be used to prompt the user for multiple
#     values which are simultaneously assigned to varriables.]

# 9. A counted loop is designed to iterate a specific number of times. T
#     [Explanation: p.43-4 "The simplest kind of loop is called a definite loop. This is a loop that will
#     execute a definite number of points. That is, at the point in the program when the loop begins, Python
#     knows how many times to go around (or iterate) the body of the loop....This particular loop pattern is
#     called a counted loop, and it is build using a Python for statement.]

# 10. In a flowchart, diamonds are used to show statement sequences, and rectangles are used for decision points.F
#     [Explanation: p.47: Other way around. "The diamond-shaped box in the flowchart represents a decision
#     in the program."]

## Multiple Choice 
#1. Which of the following is not a step in the software development process? 
#  1. Which of the following is not a step in the software development process? [C]
#     (a) specification     (b) testing/Debugging
#     (c) fee setting       (d) maintenance
#     [Explanation: p.50: The software development process involves the following steps:
#                             1. Problem Analysis
#                             2. Program Specification
#                             3. Design
#                             4. Implementation
#                             5. Testing/Debugging
#                             6. Maintenance

#  2. What is the correct formula for converting Celsius to Fahrenheit? [A]
#     (a) F = 9/5(C) + 32       b) F = 5/9(C) - 32
#     (c) F = B^2 - 4AC         d) F = (212 - 32) / (100 - 0)
#     [Explanation: p.29 "She knows that 0 degrees Celsisus (freezing) is equal ti 32 degrees
#     Fahrenheit. With this information, she computes the ratio of Fahrenheit to Celsius degrees as
#     (212-32)/(100-0) = 180/100 = 9/5. Using F to represent the Fahrenheit temperature and C for
#     Celsius, the conversion formula will have the form F = (9/5)C + k for some constant K. Plugging
#     in 0 and 32 for C and F, respectively, Susan immediately sees that k = 32. So the final formula
#     for the relationship is F = (9/5)C + 32."]

#  3. The proces of describing exactly what a computer program will do to solve a problem is called [D]
#     (a) design     (b) implementation     (c) programming     (d) specification
#     [Explanation: p.50: "Program Specification: Deciding exactly what the program will do."]

#  4. Which of the following is not a legal identifier? [C]
#     (a) spam     (b) spAm     (c) 2spam     (d) spam4U
#     [Explanation: p.31: "Python has some rules about how identifiers are formed. Every identifier must
#     begin with a letter or underscore (the "_" character) which may be followed by any sequence of
#     letters, digits, or underscores."]

#  5. Which of the following are not used in expressions? [B]
#     a) variables     (b) statements     (c) operators     (d) literals
#     [Explanation: p.32: "The simplest kind of expression is a literal." p.33: "A simple identifier
#     can also be an expression. We use identifiers as variables to give names to values." p.32: "More
#     complex and interesting expressions can be constructed by combining simpler expressions with
#     operators." p.523: "statement: A Single command in a programming langauge."]

#  6. Fragments of code that produce or calculate new data values are called [B]
#     a) identifiers            b) expressions
#     c) productive clauses     d) assignemnt statements
#     [Explanation: p.32: "The fragments of program code that produce or calculuate new data values are
#     called expressions."]

#  7. Which of the following is not a part of the IPO pattern? [B]
#     a) input     b) program     c) process     d) output
#     [Explanation: p.29: "...a standard pattern: Input, Process, Output (IPO)." As discussed in the
#     previous chapter, a program is a specific set of instructions telling a computer precisely
#     what to do step by step.]

#  8. The template for <variable> in range(<expr>) describes [D]
#     a) a general for loop     b) an assignment statement
#     c) a flowchart            d) a counted loop        
#     [Explanation: p.44: "This particular loop patter is called a counted loop.."]

#  9. Which of the following is the most accurate model of assignment in Python? [A}
#     a) sticky-note     b) variable-as-box     c) simultaneous     d) plastic-scale
#     [Explanation: p.38: "The effect is like moving a sticky note from one object to another."]

# 10. In Python, getting user input is done with a special expression called [D]
#     a) for     b) read     c) simulataneous assignment     d) input
#     [Explanation: p.39: "The purpose of an input statement is to get some information from the user of
#     a program and store it in a variable. Some programming languages have a special statemetn to do
#     this. In Python, input is accomplished using an assignment statement combined with a built-in
#     function called input."]
## Discussion

#  1. List and describe in your own words the six steps in the software development process.
#     The software development process consists of six distinct steps. Only when one is complete should
#     the next one be undertaken.
#			Problem Analysis: Studying the problem to be solved. 
#	Program specification: Deciding exactly what the program will do.
#	Design: Writing an algorithm in pseudocode.
#	Implement the design:  Translating the design into a programming language.
#	Test/debug the program: finding and fixing errors in the program
#	Maintain the program: keep the program up to date with evolving needs.

#
