#Python Program to Check Armstrong Number for 3 digits 
#A 3-digit Armstrong number is a number in which the sum of the cubes of its digits is equal to the number itself.

num=int(input("Enter a number: "))
sum=0
temp=num   #make a copy of the number because we will break this number digit by digit
while temp>0:
    digit=temp%10 #get last digit
    sum= sum+digit**3 #cube the digit and add to sum
    temp=temp//10  #Remove last digit
    
# Check if number is armstrong
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")