#Python Program to create a countdown timer

import time
t=int(input("Enter time in seconds:"))

#loop backward from t to 1      
while t:
    print(t)
    time.sleep(1)   #wait 1 second
    t-=1
print("time's up!")