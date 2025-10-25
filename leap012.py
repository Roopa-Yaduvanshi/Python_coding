#Python Program to Check Leap Year

year=int(input('Enter your year : '))

# a year is a leap year if it is divisible by 4 and not divisible by 100
if (year%4==0 and year%100!=0):
    print('{0} is a leap year'.format(year))
    
#a year is also a leap year if it is perfectly divisible by 400
elif(year%400==0):
      print('{0} is a leap year'.format(year))
else:
      print('{0} is not a leap year'.format(year))