#!/usr/bin/env python3

# Approximate age from year of birth, using datetime library

# Import datetime object to work with dates and times
import datetime

# Ask user for some text
birth_year = input('In what year were you born?')

# Turn text into integer (whole) number
birth_year = int(birth_year)

# From the datetime module, call the now() function of the datetime object,
# returning current date and time from the computer's clock
now = datetime.datetime.now()

# Now, grab the year property
current_year = now.year

# Calculate age and display result
print('Your age is:', current_year - birth_year)
