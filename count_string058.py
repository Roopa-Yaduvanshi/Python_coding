#Python Program to Count the Number of Occurrence of a Character in String

text=input("Enter a string:")
char=input("Enter the character to count:")

text = text.lower()
char = char.lower()

count=text.count(char)

print(f"The character '{char} occurs {count} times in the string")