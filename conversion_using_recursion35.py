#Python Program to Convert Decimal to Binary Using Recursion

def decimal_to_binary(n): 
#Base case:if number is greater than 1,call the function again
    if n>1:
     decimal_to_binary(n//2)
#Print remainder 0 or 1
    print(n%2,end="")
#Take input from user
num=int(input("Enter a decimal number: "))
print("Binary:", end=" ")
decimal_to_binary(num)
print()