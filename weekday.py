# stack overflow & w3 schools

import datetime

# get today's date
today = datetime.datetime.now()

# check if today is a weekday
if today in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")