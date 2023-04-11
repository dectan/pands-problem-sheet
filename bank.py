#exception handling from wk 09 lectrure
#import sys

while True:
    try:
#ask the user to enter amounts, and store in number1 + number2
        number1 = int(input('please enter amount 1 (in cent):'))
        number2 = int(input('please enter amount 2 (in cent):'))
        if number1 < 0 or number2 <0:
            raise ValueError
        break
    except ValueError as e:
        print("Both first and second number must be positive, and must not contain any symbols, ",e)
           #elif: number1 >0 and number2 >0  
number3   = (number1 + number2) / 100

print(f'the sum of these is €{number3:.2f}')
    