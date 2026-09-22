def SetZeros(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j]== 0 :
                markInfinity(matrix,i,j)

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0 

def markInfinity(matrix,row,col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        if matrix[i][col] != 0 :
            matrix[i][col] = float("inf")   
    for j in range(c):
        if matrix[row][j] != 0 :
            matrix[row][j] = float("inf")  



matrix = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

# Call function
SetZeros(matrix)

# Print result
for row in matrix:
    print(row)            
