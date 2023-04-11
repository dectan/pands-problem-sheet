# stack overflow & w3 schools
#https://poopcode.com/check-day-weekday-weekend-python/
import datetime

# get today's date, returns day of the week as(Mon:0,Tue:1,Wed:2,Thur:3,Fri:4,Sat:5,Sun:6)
today = datetime.datetime.now().weekday()
#print(today)
# check  today is less than 4, then its a weekkday
if today <4:
    print("Yes, unfortunately today is a weekday.")
#if not <4, then its the weekend
else:
   print("It is the weekend, yay!")