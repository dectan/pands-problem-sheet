#https://stackoverflow.com/questions/15374969/determining-if-a-string-contains-a-word
#https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python
#https://www.geeksforgeeks.org/python-check-whether-string-contains-only-numbers-or-not/?ref=rp


while True :
   try:
      accountnum = str(input('Please enter an 10 digit account number:'))
      if len(accountnum) != 10:
         raise ValueError("Account number entered must be 10 digits")
      #check if number entered is numerical
      if accountnum.isdigit():
         # replace last 4 digits of acountnumber  with * & format to right of string
         maskednum = accountnum[-4:].rjust(len(accountnum),'*')
         print(maskednum)
         #print(accountnum)
         #break while true
         break
         print("program ending")
      else:
         print("you must enter numbers only")
   except ValueError as e:
      print(e)