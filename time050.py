#Python Program to Convert String to Datetime

from datetime import datetime

my_date_string = "Oct 22 2025 11:59AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)