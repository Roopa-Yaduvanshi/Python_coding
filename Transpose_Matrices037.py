#Python Program to Transpose Matrix

#First of all define a matrix
A = [[10,2,3],
    [5,8,4],
    [9,7,6]]

#Creating a result matrix with zeros
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
#Transpose matrix
for i in range(len(A)):    #loop through rows
    for j in range(len(A[0])):   #loop through columns
        result[j][i] = A[i][j]
        
print("Original Matrix:")
for r in A:
    print(r)
        
#Displaying the result
print("Transposed Matrix :")
for r in result:
    print(r)