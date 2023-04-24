#https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_count
#https://stackoverflow.com/questions/30277347/if-else-statements-accepting-strings-in-both-capital-and-lower-case-letters-in-p
#using sys.argv as demonstrated in WK09 Lecture

import sys
while True:
   try:
      filename = sys.argv[1]  
   except IndexError:
      filename = input("Please enter a filename: ")  
   try:
      with open(filename,'r') as f:
         text = f.read()
         count = 0
         for i in text:
            if (i == "e"or i =="E"):
               count +=1
         print(count)
         break
#sep='' removes blanks before and after filename
   except FileNotFoundError:
               print("filename (", filename,") does not exist. Please re-run and enter a valid filename",sep = '')