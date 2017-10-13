#!/usr/bin/env python3

# Properly calculate age from year of birth, using datetime library

# Import datetime object to work with dates and times
import datetime

# Ask user for some text
birth_date = input('On what date were you born? (YYYY-MM-DD) ')

# Parse string into datetime
birth_date_obj = datetime.datetime.strptime(birth_date, '%Y-%m-%d')

# You can print the date object, formatted
print('You were born on', birth_date_obj.date().isoformat())

# Now calculate difference from today
difference = datetime.datetime.now() - birth_date_obj

# Take the amount of years in the difference (let's hope nobody was born in a leap year!)
age = int(difference.days/365)

# Calculate age and display result
print('Your age is:', age)
