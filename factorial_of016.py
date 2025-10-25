#Python Program to Find the Factorial of a Number

#Method1
num=int(input('Enter a number : '))
factorial=1
if num<0:
    print('sorry, Factorial does not exist for negative number')
elif num==0:
    print('The factorial of 0 is 1')
for i in range(1,num+1):
   factorial=factorial*i
   print("The factorial of", num, "is" ,factorial)
    
    
    
#Method 2   factorial of a number using recursion
def factorial(x):
     if x==0 or x==1:
      return 1
     else:
      return (x*factorial(x-1))
        
num=int(input('Enter a number: '))
result=factorial(num)
print("The factorial of", num ,"is",result)   