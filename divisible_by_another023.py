#Python Program to Find Numbers Divisible by Another Number

#list of numbers
list=[10,25,30,15,50,60]

#take divisor from user
divisor=int(input("Enter a number to divide by: "))
print("Number divisible by", divisor,"are")

for num in list:
    if num%divisor==0:  #check divisibility
        print(num)