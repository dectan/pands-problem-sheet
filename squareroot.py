#https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

import sys
def sqrt(x):

   x = (number / 2)
   tolerance = .00001
    # keep iterating until y -x < .001
   while True:
        #calculate y 
        y = (x + number/x) / 2
        #print(y)

        # check if the absolute difference between y - x is < .00001
        if abs(y - x) < tolerance:
            #print(y)
            # return y to 2 decimal places as per screenshot in question.
            return round(y, 1)

        # update the values for next iteration
        x = y
try:
   number = float(input("Please enter a positive number: "))
   if number > 0:
   #output printed is formatted as per screenshot in question
      print(f"The square root of ",(number)," is ",(sqrt(number)),'.',sep = '' )

   if number <=0:
      print("Number entered must be positive, and must not contain symbols")
    
except ValueError as e:
    print("Number entered must be positive2, and must not contain symbols",e)


