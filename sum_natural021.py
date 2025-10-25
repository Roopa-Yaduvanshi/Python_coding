#Python Program to Find the Sum of Natural Numbers
num=(int(input("Enter a number: ")))
sum=0
for num in range(1,num+1):
    
    sum=sum+num
    print("Sum of first",num ,"natural number are",sum)
    
    
#Method2 by using formula
num=(int(input("Enter a number: ")))
sum=num*(num+1)/2
print("Sum of first",num ,"natural number are",sum)