import matrix as mtx
import copy

def chio(mat):
    mat = mtx.matrix(copy.deepcopy([row[:] for row in mat]))
    neg_det = False
    if mat.size() == (1, 1):
        return mat[0][0]
    
    if (mat.size()[0]) != (mat.size()[1]):
        raise ValueError("Matrix must be squared")
    n = mat.size()[0]
    pivot = mat[0][0]
    
    if all(mat[0][i] == 0 for i in range(n)) or all(mat[i][0] == 0 for i in range(n)):
        return 0
    
    if pivot == 0:
        for i in range(n):
            if mat[0][i] != 0:
                for j in range(n):
                    mat[j][0], mat[j][i] = mat[j][i], mat[j][0]
                pivot = mat[0][0]
                neg_det = not neg_det
                break
            
    
    if mat.size() == (2, 2):
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    next_mat = []
    temp_row = []
    

    for R in range(1, n):
        for C in range(1, n):
            temp_row.append(mat[0][0]*mat[R][C] - mat[0][C]*mat[R][0])
        next_mat.append(temp_row)
        temp_row = []

    if neg_det:
        neg_det = False
        return -(1/(pivot**(n-2))*chio(mtx.matrix(next_mat)))
    else:
        return (1/(pivot**(n-2))*chio(mtx.matrix(next_mat)))


mat1 = mtx.matrix([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

] )

deter1 = chio(mat1)

print(deter1)

mat2 = mtx.matrix( [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ] )

deter2 = chio(mat2)
print(deter2)

mat3 = mtx.matrix([
     [0 , 0 , 0 , 0 , 0],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

deter3 = chio(mat3)
print(deter3)

mat4 = mtx.matrix( [
     [0 , 1 , 1 , 2 , 3],
     [0 , 2 , 1 , 7 , 3],
     [0 , 1 , 2 , 4 , 7],
     [0 , 1 , 0 , 7 , 0],
     [0 , 4 , 7 , 2 , 2]
    ])

deter4 = chio(mat4)
print(deter4)