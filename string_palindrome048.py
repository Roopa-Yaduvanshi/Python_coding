#Python Program to Check Whether a String is Palindrome or Not

# take input from user
my_str=input("Enter a string:")

# convert to lowercase to ignore case (like 'Madam' = 'madam')
my_str=my_str.lower()

# reverse the string
reverse_str=my_str[::-1]

#check if original and reversed are same
if my_str==reverse_str:
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")