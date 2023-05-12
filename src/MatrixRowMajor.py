class MatrixRowMajor:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def getCell(self, x, y):
        return self.matrix[x][y]
    
    def giveMatrix(self):
            return self.matrix