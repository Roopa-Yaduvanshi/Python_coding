#Python Program to Display Powers of 2 Using Anonymous Function

n=int(input("Enter how many terms: "))  #ask use how many power to print

#lambda function (anonymous)
power=lambda x: 2**x

#Loop to print powers of 2
for i in range(n):
 print("2^",i,"=",power(i))