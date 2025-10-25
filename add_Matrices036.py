#Python Program to Add Two Matrices

#First of all define two matrices
A = [[1,2,3],
    [2,3,4],
    [4,5,6]]

B = [[4,2,3],
    [2,5,4],
    [1,5,3]]

#Creating a result matrix with zeros
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
#Adding two matrices
for i in range(len(A)):    #loop through rows
    for j in range(len(A[0])):   #loop through columns
        result[i][j] = A[i][j] + B[i][j]
        
        #Displaying the result
for r in result:
    print(r)