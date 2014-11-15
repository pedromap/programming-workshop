# Ask people for their age and calculate the mean

# Create empty list to store ages
ages = []

# Ask first age
result = input('What\'s your age? ')

# Keep asking while result is higher than zero
while result > 0:
    # Add age to list
    ages.append(result)

    # Ask for age
    result = input('What\'s your age? ')

# Calculate the mean
total = 0
for age in ages:
    # The following two lines are equivalent, the lower is a shortcut
    total = total + age
    total += age

# len(<thing>) yields the size of the thing
mean = total/len(ages)
print 'Mean age:', mean
