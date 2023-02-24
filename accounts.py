accountnum = str(input('Please enter an 10 digit account number:'))

maskednum = accountnum[-4:].rjust(len(accountnum), '*')
print(maskednum)

