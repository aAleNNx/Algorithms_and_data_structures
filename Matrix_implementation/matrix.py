import copy

class matrix:
    def __init__(self, data, fill = 0):
        if isinstance(data, tuple):
            if len(data) != 2:
                raise ValueError("Tuple must contain only row and column")
            row, col = data
            if row <= 0 or col <= 0:
                raise ValueError("Matrix cannot be empty")
            self.__row = row
            self.__col = col
            self.__matrix = []
            for _ in range(row):
                (self.__matrix).append([fill for _ in range(col)])
                
        
        else:
            if len(data) <= 0:
                raise ValueError("Matrix cannot be empty")
            if len(data[0]) <= 0:
                raise ValueError("Matrix cannot be empty")
            if any(len(row) != len(data[0]) for row in data):
                raise ValueError("All rows must have the same length")
            if not all(isinstance(row, list) for row in data):
                raise TypeError("Matrix must be a list of lists")
            self.__matrix = copy.deepcopy(data)
            self.__row = len(data)
            self.__col = len(data[0])
        
    def size(self):
        return (self.__row, self.__col)
        
    def __getitem__(self, row):
        if not isinstance(row, int):
            raise TypeError("Index must be int")
        if row >= self.__row or row < 0:
            raise IndexError("Row index out of range")
        
        return self.__matrix[row]
        
    def __add__(self, other):
        if not isinstance(other, matrix):
            raise TypeError("Operand must be matrix")
    
        if self.size() != other.size():
            raise ValueError("Matrices must have the same size")
        result = []
        temp_row = []
        
        for R in range (self.__row):
            for C in range (self.__col):
                temp_row.append(self[R][C] + other[R][C])
            result.append(temp_row)
            temp_row = []
        return matrix(result)
                    
    def __str__(self):
        result = ""
        for row in self.__matrix:
            result += '|' + " ".join(str(elem) for elem in row) + '|\n'
        return result

    def __mul__(self, other):
        if not isinstance(other, matrix):
            raise TypeError("Operand must be matrix")

        row, column = other.size()

        if self.__col != row:
            raise ValueError("Wrong dimensions for multiplication")
        
        result = []
        temp_row = []
        
        for R in range (self.__row):
            for C in range (column):
                temp_row.append(sum([(self[R][n] * other[n][C]) for n in range (row)]))
            result.append(temp_row)
            temp_row = []
        return matrix(result)
        
    def __eq__(self, other):
        if not isinstance(other, matrix):
            return False
        if self.size() != other.size():
            return False
        for R in range(self.__row):
            for C in range(self.__col):
                if self[R][C] != other[R][C]:
                    return False
        return True