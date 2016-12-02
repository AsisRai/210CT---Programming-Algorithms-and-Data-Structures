""" WRite the pseudocode corresponding to functions for addition, subtraction and
multiplication of two matricies. Computer A = B*C-2*(B+C) """

#Pseudocode

"""

GLOBAL A ← [[1,2,1],[0,1,0],[2,3,4]]
GLOBAL B ← [[2,5,1],[6,7,1],[1,8,1]]

C ← [[0,0,0],[0,0,0],[0,0,0]]
D ← [[0,0,0],[0,0,0],[0,0,0]]
E ← [[0,0,0],[0,0,0],[0,0,0]]

ADDITION(A,B)
    for column in range(A) 
        for row in range(B[0]) 
            C[column][row] ← A[column][row] + B[column][row] 

SUBTRACTION(A,B)
    for column in range(A)
        for row in range(B[0])
            D[column][row] ← A[column][row] - B[column][row]

MULTIPLY(A,B)
    for column in range(A)
        for row in range(B[0])
            for column in range(B)
                E[column][row] ← A[column][row] + B[column][row]
            
"""
#Python code

matrix1 = [[1,2,1],[0,1,0],[2,3,4]]
matrix2 = [[2,5,1],[6,7,1],[1,8,1]]

addition = [[0,0,0],[0,0,0],[0,0,0]]
scale = [[0,0,0],[0,0,0],[0,0,0]]
multiply = [[0,0,0],[0,0,0],[0,0,0]]
compute = [[0,0,0],[0,0,0],[0,0,0]]

print("Matrix1 = ", matrix1)
print("Matrix2 = ", matrix2)
    
def COMPUTE(): #(B+C),2*(B+C), B*C and finally matrix of  B*C - matrix of 2*(B+C)

    for i in range(len(matrix1)):#iterates over colums of matrix1 #n
        for y in range(len(matrix2[0])): #iteraes over rows of matrix2 ##[0]because it only needs the length of 1 row since all rows are same size #n*n
            addition[i][y] = matrix1[i][y]+matrix2[i][y] #adds colums of matrix1 and rows of matrix together and stores it in addition matrix #1

    for i in range(len(addition)):  #n 
        for y in range(len(addition[0])):#n*n 0(n^2)
            scale[i][y] = addition[i][y]+addition[i][y]#1  #adds colums of addition matrix and rows of addition matrix together and stores it in scale matrix
                                                         #this is because 2*(B+C) is equivalent to (B+C) + (B+C)

    for i in range(len(matrix1)): #n
       for y in range(len(matrix2[0])):#n*n
           for k in range(len(matrix2)):#n*n*n 0(n^3)
               multiply[i][y] += matrix1[i][k] * matrix2[k][y] #1

    for i in range(len(multiply)):  
        for y in range(len(scale[0])):
            compute[i][y] = multiply[i][y] - scale[i][y] 
    

    print('Addition = (B+C) ======== : ', addition)
    print('Scale = 2*(B+C) ======== : ',scale)
    print('Multiply = B*C ======== : ',multiply)
    print('Compute B*C - matrix of 2*(B+C)')
    print('The answer is : ', compute)

COMPUTE()

#Runtime = 0(n^3)
    
    
    

    
    

    
    

    
