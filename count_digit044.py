#Python Program to count the number of Digits Present in a Number
 
num=int(input("Enter a number:"))

count=0

#repeat until number becomes 0
while num!=0:
    num//=10
    count+=1
    
print("Total digits:",count)