#ask the user to enter amounts, and store in number1 + number2
number1 = float(input('please enter amount 1 (in cent):'))
number2 = float(input('please enter amount 2(in cent):'))

#calculation done and stored in num3
number3   = (number1 + number2) / 100

#print number 3 to 3 decimal places
print (f'the sum of these is €{number3:.2f}')
