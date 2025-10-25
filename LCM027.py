#Python Program to find LCM
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# Find the greater number
if num1 > num2:
    greater = num1
else:
    greater = num2

while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break
    greater += 1

print(f"The LCM of {num1} and {num2} is: {lcm}")

#Method 2 Using Euclidean Formula
def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // hcf(a, b)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
