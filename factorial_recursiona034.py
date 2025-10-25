# Python Program to Find Factorial of Number Using Recursion
# The factorial of n is:
# n!= n * (n-1) * (n-2) *.....*1

def factorial(n):
    #Base Condition
    if n==1:
        return n
    else:
        return n*factorial(n-1) 
    
#Taking user input
num=int(input("Enter a number:"))
if num<0:
    print("Enter a positive number")
elif num==0:
     print("The factorial of 0 is 1")
else:
     print("The factorial of", num, "is", factorial(num))