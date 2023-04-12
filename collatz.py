#https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
#https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
#exception handling from wk 09 lectrure
#import sys

#if valid user input, program moves to next step
while True:
    try:
        #if statement to ensure number is positive and numeric
        num = int(input("Please enter a positive integer:"))
        if num <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.",e)

while num !=1:
    #use end =' ' to print number on same line in terminal 
    print(num, end=' ')
    # even number if no remainder
    if num % 2 == 0:
        num //= 2
    else:
        #if not even number then must be Odd number 
        num = num * 3 + 1
#question asked for 1 to be printed, so by printing num while num = 1, 1 gets printed
print(num)