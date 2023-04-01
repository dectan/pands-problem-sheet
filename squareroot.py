

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points



def sqrt(x):
   tolerance = 0.000001
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate
 

   
x = float(input("Please enter a positive number: "))
if x >0:
         #print("Number must be positive")
         x = float(x)
         print("The program's estimate is", sqrt(x))
if x <=0:
         print("Number entered must be positive")
else:
         print("Number must not contain any symbols")