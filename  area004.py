#Program to find area of right angle triangle
base=float(input("enter the base of a triangle: "))
height=float(input("enter the height of a triangle: "))
area=0.5*base*height
print("Area of triangle is:", area)


#area of triangle with given three sides
import math
a=float(input("enter first side: "))
b=float(input("enter second side: "))
c=float(input("enter third side: "))
#calculate semi-perimeter
s = (a+b+c) / 2
#calculate area using heron's formula
area = math.sqrt( s * (s-a) * (s-b) * (s-c) )
print("Area of triangle is:", area)


#other way to write a code
a=float(input("enter first side: "))
b=float(input("enter second side: "))
c=float(input("enter third side: "))
#calculate semi-perimeter
s = (a+b+c) / 2
#calculate area using heron's formula
area = (s * (s-a) * (s-b) * (s-c) )**0.5
print("Area of triangle is:", area)
        