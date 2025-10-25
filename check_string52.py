#Python Program to Check If a String Is a Number (Float)

#take input from user
string=input("Enter a string:")

#try converting the string to float
try:
    float(string)
    print("Yes, the string is a number (float).")
except ValueError:
    print("No, the string is not a number.")