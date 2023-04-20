#exception handling from wk 09 lectrure
#https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division
#import sys
#if valid user input, program moves to next step
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
number3 = (number1 + number2)
#// to calculate qty of euros in number3 with floor division
euros = number3 // 100
print(euros)
#modulus to calculate the qty of cents
cents = number3 % 100
#print euros & cents formatted to 2 decimal places
print(f"The sum of these is €{euros}.{cents:02d}")
