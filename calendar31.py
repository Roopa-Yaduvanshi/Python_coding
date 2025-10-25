#Python Program to Display Calendar

import calendar
#input year and month
year=int(input('Enter Year: '))
month=int(input('Enter Month: '))
#display the calendar
print(calendar.month(year,month))