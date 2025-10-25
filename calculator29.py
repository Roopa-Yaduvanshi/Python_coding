#Python Program to Make a Simple Calculator
#Simple Calculator
print('Select operation: ')
print("1. Addition(+)")
print('2. Subtraction(-)')
print('3. Multiplication(*)')
print('4. Division(/)')
#Take input from the user
choice=input("Enter choice (1/2/3/4):")
num1=float(input("Enter Ist number: "))
num2=float(input("Enter 2nd number : "))
if choice=='1':
    print("Result:", num1+num2)
elif choice=='2':
    print('Result:',num1-num2)
elif choice=='3':
    print('Result:', num1*num2)
elif choice=='4':
    if num2!=0:
        print('Result:', num1/num2)
    else:
        print('Division is not possible')
else:
        print('Invalid Input')