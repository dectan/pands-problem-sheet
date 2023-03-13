#while loop & for loops lab wk 03

accountnum = str(input('Please enter an 10 digit account number:'))
while len(accountnum) != 10:
    if accountnum == 10:
  # accountnum = str(input('Account Number must be exactly 10 digits:'))
   #else
     maskednum = accountnum[-4:].rjust(len(accountnum), '*')
    print(maskednum)

