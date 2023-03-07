

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points



def newton(x):
   tolerance = 0.000001
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate
 
def start():
   
       x = input("Please enter a positive number: ")
       x = float(x)
       print("The program's estimate is", newton(x))
       
start()