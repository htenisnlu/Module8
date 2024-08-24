# Hikmet Tenis
# 08/17/2024
# This function that takes a year as a parameter and 
# returns True if the year is a leap year, False if it is otherwise.

def is_leap_year(year):
    # Check if the year is a leap year
    # A year is a leap year if it is divisible by 4, but not divisible by 100, 
    # unless it is also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
