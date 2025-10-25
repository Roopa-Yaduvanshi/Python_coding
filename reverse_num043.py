#Python Program to reverse a number

#Take user input
num=int(input("Enter a number:"))

rev=0  #to store reversed number

#repeating the condition until numbet becomes 0
while num != 0:
    digit = num % 10  #get last digit
    rev = rev * 10 + digit  #add it to the reverse
    num = num // 10      #remove last digit
    
    print("Reversed number:", rev)