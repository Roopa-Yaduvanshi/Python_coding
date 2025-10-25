#Python Program to Measure the Elapsed Time in Python 

import time 

#Step1- Record start time
start= time.time()
print("Start time :",start)

#Step2- Some code whose time we want to measure
sum=0
for i in range(1000000):
    sum=sum+i
    
#Step3= Record end time
end=time.time()
print("End time:",end)

#Step4= Difference between both times
elapsed_time=end-start
print("Elapsed time:",elapsed_time,"seconds")