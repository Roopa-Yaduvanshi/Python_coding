#program to find the square root of number
import math
num =36
result = math.sqrt(num) 
print("Square root is:", result)


#program to find square root of number by user input
import math 
#take the user input
num=float(input("Enter a number: "))
#calculate the square root
result = math.sqrt(num)
print("the square root is:", result)


# 3rd method
num = 8 
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

#other way
num=float(input("enter a num: "))
result=num**0.5
print("the square root of %0.3f is %0.3f"%(num,result))
