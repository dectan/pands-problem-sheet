#https://stackoverflow.com/questions/15374969/determining-if-a-string-contains-a-word
#https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python


import sys

try:
  accountnum = str(input('Please enter an 10 digit account number:'))
  if len(accountnum) != 10:
     raise ValueError("Account number entered must be 10 digits & must be a positive number")
  if '-' in accountnum:
     raise ValueError("Account number entered must be a positive number")
 #   if accountnum == 10:
  #accountnum = str(input('Account Number must be exactly 10 digits:'))
   #else
  maskednum = accountnum[-4:].rjust(len(accountnum),'*')
  print(maskednum)
except ValueError as e:
    print(e)














