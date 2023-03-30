#https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_count

#using sys.arg as demonstrated in WK09 Lecture

import sys
 
filename = sys.argv[1]  

try:
    with open(filename,'r') as f:
       text = f.read()
       count = text.count("e")
       print(count)

except FileNotFoundError:
   print("file does not exist")
