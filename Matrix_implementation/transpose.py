import matrix

def transpose(mat):
    tran = []
    temp_row = []
    rows, cols = mat.size()
    for C in range(cols):
        for R in range(rows):
            temp_row.append(mat[R][C])
        tran.append(temp_row)
        temp_row = []

        
    return matrix.matrix(tran)