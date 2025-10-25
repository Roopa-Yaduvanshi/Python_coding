#Python Program to Print the Fibonacci sequence

num=int(input("Enter a number: "))
a=0
b=1

# Program to display the Fibonacci sequence up to n-th term
if num<=0:
        print("Enter a positive number.")
elif num==1:
        print(a)
else:
        print('fibonacci series are:')
        #print first two terms
        print(a)
        print(b)
for i in range(2,num):

        c=a+b
        print(c)
        a=b
        b=c