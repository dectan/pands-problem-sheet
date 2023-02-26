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


number = int(input('Please enter a positive integer:'))
collatz(number)
