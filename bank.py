
import sys

try:
#ask the user to enter amounts, and store in number1 + number2
    number1 = float(input('please enter amount 1 (in cent):'))
    #if number1 > 0:
    number2 = float(input('please enter amount 2(in cent):'))
    if number1 and number2 > 0:
#calculation done and stored in num3
        number3   = (number1 + number2) / 100

#print number 3 to 2 decimal places
        print(f'the sum of these is €{number3:.2f}')

    else:
        print("you must enter numbers only")
    
except ValueError as e:
    print("Please enter a valid number as",e)
