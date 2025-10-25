#Python Program to Sort Words in Alphabetic Order 

#Take input from user
sentence=input("Enter a sentence:")

#split the sentence into words
words=sentence.split()

#sort the words alphabetically
words.sort(key=str.lower)

print("Words in alphabetical order:")
for word in words:
    print(word)