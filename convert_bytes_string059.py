#Python Program to Convert Bytes to a String

data=b'Hello World'

#convert bytes to string
text=data.decode('utf-8')

print("Bytes data:", data)
print("String data:", text)


# Python Program to Convert String into Bytes

text = input("Enter a string: ")

# convert string to bytes using encode()
bytes_data = text.encode('utf-8')

print("Original string:", text)
print("Bytes data:", bytes_data)