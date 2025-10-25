#Python Program to Get a Substring of a String

#take input from user
string=input("Enter a string:")

#get starting and ending index from string
start=int(input("Enter a starting index:"))
end=int(input("Enter a ending index:"))
 
#extract substring using slicing     
substring=string[start:end]

#printing the result
print("Substring is:",substring)