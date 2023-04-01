#https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
import sys


def collatz(number):
    if number % 2 == 0:           # Even number
        number = number // 2
    elif number % 2 == 1:         # Odd number
        number = (3 * number) + 1

    while number == 1:            
        print(number)
        sys.exit()                

    while number != 1:            
        print(number)
        number = number           
        return collatz(number)    

try:
    number = int(input('Please enter a positive integer:'))
    if number > 0:
        collatz(number)
    if number < 0:
        print("No Negative numbers")

    else:
        print("Number must be greater than 0")
        print(number)

except ValueError as e:
    print('Please enter a valid number with no symbols')
    #print(f'Please enter a valid number with no symbols',e)
    
