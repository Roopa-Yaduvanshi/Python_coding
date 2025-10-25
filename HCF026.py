#Python Program to Find HCF or GCD
# Method 1: Using the math.gcd function
import math
num1=int(input("Enter a 1st number : "))
num2=int(input("Enter 2nd number : "))
hcf=math.gcd(num1,num2)
print(f"The hcf of {num1} and {num2} is: {hcf}")

# Method 2: Using Euclidean Algorithm
def hcf(a,b):
    while b!=0:   #repeat until reminder is 0
     temp = a
     a = b
     b = temp % b
    return a
num1=int(input("Enter a 1st number : "))
num2=int(input("Enter 2nd number : "))
print(f"The hcf of {num1} and {num2} is: {hcf(num1,num2)}")