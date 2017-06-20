# Name: Arianna
# Date: 6/20/17

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""


var=raw_input("How many Fibonacci numbers do you want to generate?")
print var

var=int(var)



answer1=1

previous=0

for variable in range (0,var):
    print answer1
    answer2= answer1+previous
    previous=answer1
    answer1=answer2


    # answer1=2



    # previous=1
    # answer2= answer1+answer2
    #
    # for variable in range (0,var):
    #     answer=answer2
    #     print answer




