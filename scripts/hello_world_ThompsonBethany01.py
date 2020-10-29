// LANGUAGE: Python
// ENV: VS Code
// AUTHOR: Bethany Thompson
// GITHUB: https://github.com/ThompsonBethany01

'''
Run this script to print a greeting specific to the current time
Morning, Afternoon, Evening, or Night
'''
# imports function to find current hour
from datetime import datetime

# sets variable to hour of the current time
current_hour = datetime.now().time().hour

# loops to determine what greeting to print, range does not include second value
# if hour is from 6am to 11am
if current_hour in range(6,12):
    print('Good Morning, World')

# if hour is from 12 pm to 5 pm
elif current_hour in range(12,18):
    print('Good Afternoon, World')

# if hour is from 6pm to 9pm
elif current_hour in range(18,22):
    print('Good Evening, World')

# if hour is from 10pm to 5am
elif current_hour >= 22 or current_hour < 6:
    print('Good Night, World')
