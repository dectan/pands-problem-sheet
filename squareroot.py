

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# struggling with this as dont fully understand how it works.

def newton(x):
   tolerance = 0.000001
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate
 

def main():
   while True:
       x = input("Please enter a positive number: ")
       if x == '':
           break
       x = float(x)
       print("The program's estimate is", newton(x))
       
main()