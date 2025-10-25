## Python Program to Parse a String to a Float or Int

# take input from user
num_str = input("Enter a number: ")

# check if the string contains a decimal point
if "." in num_str:
    # convert to float
    num = float(num_str)
    print("Parsed number (float):", num)
else:
    # convert to integer
    num = int(num_str)
    print("Parsed number (int):", num)