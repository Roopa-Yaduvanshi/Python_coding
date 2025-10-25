#Python Program to Find Armstrong Number in an Interval

start=int(input("Enter a number: "))
end=int(input("Enter a number: "))

print("Armstrong number between",start, "and",end ,"are:")
for num in range(start,end+1):   #loop through all number in an interval 
  sum=0
  temp=num   #make a copy of the number because we will break this number digit by digit
  while temp>0:
    digit=temp%10 #get last digit
    sum= sum+digit**3 #cube the digit and add to sum
    temp=temp//10  #Remove last digit
    
# Check armstrong condition
  if num==sum:
    print(num)