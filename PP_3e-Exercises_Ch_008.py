#Review Questions
#True/ False
#1. A Python while implements a definite loop. False
#Reference page 266:A Python for loop is a definite loop that iterates through a sequence.
#                   • A Python while statement is an example of an indefinite loop
#2. The counted loop pattern uses a definite loop. True
# counted loop A loop written to iterate a specific number of times
#3. A sentinel loop asks the user whether to continue on each iteration.
#Reference page 247:The idea behind an interactive loop is that it allows the user to repeat certain portions of a
program on demand. 
#4. A sentinel loop should not actually process the sentinel value.True
#Reference page249:The sentinel is not processed as part of the data.

#5. The easiest way to iterate through the lines of a file in Python is to use a while loop.?

#6. A while is a post-test loop. True
#Reference page263: Unlike some other languages, Python does not have a statement that directly implements a post-test
# loop. However, this algorithm can be implemented with a while by "seeding" the loop condition for the first iteration

#7. The Boolean operator or returns True when both of its operands are true.True

#8. a and (b or c) == (a and b) or (a and c)  True
#Reference page 260

#9. not(a or b) -- (not a) or not(b) False
#Reference page 261:( not(a or b) ) == ( (not a) and (not b) )
#10. True or False


#Multiple Choice
#1 . A loop pattern that asks the user whether to continue on each iteration is called a(n) a)
a) interactive loop* b) end-of-file loop c) sentinel loop d) infinite loop

2. A loop pattern that continues until a special value is input is called a(n)
a) interactive loop b) end-of-file loop c) sentinel loop* d) infinite loop

3. A loop structure that tests the loop condition after executing the loop body is called a
a) pre-test loop b) loop and a half c) sentinel loop d) post-test loop*

4. A priming read is part of the pattern for a(n)
a) interactive loop b) end-of-file loop c) sentinel loop* d) infinite loop 

5. What statement can be executed in the body of a loop to cause it to terminate?
a) if b) input c) break* d) exit

6. Which of the following is not a valid rule of Boolean algebra?
a) (True or x) == True
b) (False and x) == False
c) not(a and b)== not(a) and not(b) *false
d) (True or False) == True

7. A loop that never terminates is called
a) busy b) indefinite c) tight d) infinite*

8. Which line would not be found in a truth table for and?
a) T T T b) T F T* c) F T F d) F F F

9. Which line would not be found in a truth table for or?
a) T T T b) T F T c) F T F* d) F F F

10. The term for an operator that may not evaluate one of its subexpressions is
a) short-circuit* b) faulty c) exclusive d) indefinite

#Discussion

#1 . Compare and contrast the following pairs of terms:
a) definite loop vs. indefinite loop
b) for loop vs. while loop
c) interactive loop vs. sentinel loop
d) sentinel loop vs. end -of-file loop

#2. Give a truth table that shows the Boolean value of each of the following Boolean expressions, for every possible combination of "input" values.
Hint: Including columns for intermediate expressions is helpful.
a) not (P and Q)  ------> not (P) or not (Q)
b) (not P) and Q   ------>
c) (not P) or (not Q)  ------> not (P and Q)
d) (P and Q) or R  ------> (e)
e) (P or R) and (Q or R)

#3. Write a while loop fragment that calculates the following values:
a) Sum of the first n counting numbers: 1 + 2 + 3 + . . . + n

b) Sum of the first n odd numbers: 1 + 3 + 5 + . . . + 2n - 1

c) Sum of a series of numbers entered by the user until the value 999 is entered. Note: 999 should not be part of the sum.

d) The number of times a whole number n can be divided by 2 (using integer division) before reaching 1 (i.e., log2n) .
