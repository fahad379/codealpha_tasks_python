# -*- coding: utf-8 -*-
import time
from calendar import isleap
from datetime import datetime

# Judge if it's a leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

# Returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

# Get current system date
localtime = time.localtime(time.time())

# Get user's birthdate input
name = input("Input your name: ")
birth_year = int(input("Input your birth year: "))
birth_month = int(input("Input your birth month (1-12): "))
birth_day = int(input("Input your birth day: "))

# Calculate the user's age
birthdate = datetime(birth_year, birth_month, birth_day)
current_date = datetime(localtime.tm_year, localtime.tm_mon, localtime.tm_mday)

# Calculate difference in years, months, and days
age_years = current_date.year - birthdate.year
age_months = current_date.month - birthdate.month
age_days = (current_date - birthdate).days

# Adjust for negative months or days if necessary
if age_months < 0:
    age_years -= 1
    age_months += 12
if current_date.day < birthdate.day:
    age_months -= 1
    days_in_previous_month = month_days(current_date.month - 1 if current_date.month > 1 else 12, judge_leap_year(current_date.year))
    age_days = days_in_previous_month - (birthdate.day - current_date.day)

print(f"{name}'s age is {age_years} years, {age_months} months, and {age_days} days.")
