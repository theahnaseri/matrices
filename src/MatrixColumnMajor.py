class MatrixColumnMajor:
    def __init__(self, matrix):
        rowSize = len(matrix)
        columnSize = len(matrix[0])
        self.matrix = [[0 for y in range(rowSize)] for x in range(columnSize)]
        for i in range(rowSize):
            for j in range(columnSize):
                self.matrix[j][i] += matrix[i][j]

    def getCell(self, x, y):
        return self.matrix[y][x]
    
    def giveMatrix(self):
            return self.matrix