#Python Program to Multiply Two Matrices

#First of all define two matrices
A = [[1,2,3],
     [4,5,6]]

B = [[7,8],
     [9,10],
     [11,12]]

#Creating a result matrix with zeros
result = [[0,0],
          [0,0]]
#Multiplying two matrices
for i in range(len(A)):    
    for j in range(len(B[0])):  
        for k in range(len(B)): 
         result[i][j] += A[i][k] * B[k][j]
        
#Displaying the result
print("Resultant Matrix : ")
for r in result:
    print(r)