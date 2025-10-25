#Python Program to Remove Punctuations From a String

#define punctuations marks

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#Take input from user

my_str=input("Enter a string:")

#creating empty punctuation to store result
no_punct=""

#iterate through characters
for char in my_str:
    if char not in punctuations:
        no_punct=no_punct+char
        
print("String after removing punctuations:", no_punct)