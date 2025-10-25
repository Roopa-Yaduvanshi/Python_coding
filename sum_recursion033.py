#Python Program to Find Sum of Natural Numbers Using Recursion

def sum(n):
    if (n==0):
        return n
    else:
     return n+sum(n-1)

n=int(input("Enter a number of terms:"))

if n<0:
    print("Enter a positive number")
    
else:
     print("The sum of natural number using recursion is", sum(n))