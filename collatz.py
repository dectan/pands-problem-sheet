#https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
import sys

def collatz(number):
    # even number if no remainder
    if number % 2 == 0:           
        number = number // 2
    #Odd number if remainder
    elif number % 2 == 1:         
        number = (3 * number) + 1
    #end when number is 1
    while number == 1:            
        print(number)
        sys.exit()                

    while number != 1:            
        print(number)
        number = number           
        return collatz(number)    

try:
    number = int(input('Please enter a positive integer:'))
    #check if number is positive
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
    
