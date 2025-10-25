#Method 1
#Python Program to Solve Quadratic Equation
import cmath       #import complex math module to finding square root of negative number
#Quadratic equation ax^2+ bx +c =0
a=1
b=5
c=6
D=(b**2)-(4*a*c )    #finding discriminant
#finding two solution
sol1=(-b+cmath.sqrt(D))/(2*a)
sol2=(-b-cmath.sqrt(D))/(2*a)
print("The solution are {0} and {1} ".format(sol1,sol2))

#method2
import cmath        #import complex math module to handle both real and complex roots
a=float(input("Enter the value of a : "))
b=float(input("Enter the value of b : "))
c=float(input("Enter the value of c : "))
D=(b**2)-(4*a*c)                  #Finding discriminant
#finding two solution
sol1=(-b+cmath.sqrt(D))/(2*a)
sol2=(-b-cmath.sqrt(D))/(2*a)
print("The solution are {0} and {1} ".format(sol1,sol2))

#method3
import math        #import math module to finding square root of a real number 
a=float(input("Enter the value of a : "))
b=float(input("Enter the value of b : "))
c=float(input("Enter the value of c : "))
D=(b**2)-(4*a*c)                  #Finding discriminant

if D>0:
    root1= (-b+ math.sqrt(D)) / (2*a)
    root2= (-b- math.sqrt(D)) /(2*a)
    print("Two Real Roots : ", root1,root2)
elif D==0:
    root=-b/(2*a)
    print("One Real Root :", root)
else:
   real_part=-b /(2*a) 
   imaginary_part= math.sqrt(D)/(2*a)
   print("Roots :",real_part, "+" ,imaginary_part, "i",real_part, "-" ,imaginary_part, "i")
 
