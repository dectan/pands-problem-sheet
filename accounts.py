#https://stackoverflow.com/questions/15374969/determining-if-a-string-contains-a-word
#https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python
#https://www.geeksforgeeks.org/python-check-whether-string-contains-only-numbers-or-not/?ref=rp


import sys

try:
  accountnum = str(input('Please enter an 10 digit account number:'))
  if len(accountnum) != 10:
     raise ValueError("Account number entered must be 10 digits")

  if accountnum.isdigit():
   maskednum = accountnum[-4:].rjust(len(accountnum),'*')
   print(maskednum)
  else:
   print("you must enter numbers only")
except ValueError as e:
   print(e)