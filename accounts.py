#https://stackoverflow.com/questions/15374969/determining-if-a-string-contains-a-word
#https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python
#https://www.geeksforgeeks.org/python-check-whether-string-contains-only-numbers-or-not/?ref=rp


try:
   account_num = str(input("Please enter an account number: "))
#check if input is greater than 4 digits
   if len(account_num) <= 4:
      raise ValueError("Account number entered must be 10 digits")
   if account_num.isdigit():
   #create new string of * for lenght of account num -4 digits, + the last 4 digits of original account number
    masked_num = "X" * (len(account_num) - 4) + account_num[-4:]
    print(masked_num)

   else:
      print("only numbers can be entered")

except ValueError as e:
   print(f"Error:",e)