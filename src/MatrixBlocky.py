class MatrixBlocky:
     def __init__(self, matrix):
          self.rowSize = len(matrix)
          self.columnSize = len(matrix[0])
          self.matrix = []
          block = []
        
          # row:odd column:odd
          if (not isEven(self.rowSize)) and (not isEven(self.columnSize)):
               i = 0
               j = 0
               block = [matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2], matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
               self.matrix.append(block)
               block = []
               for j in range(3, self.columnSize, 2):
                    block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1], matrix[i+2][j], matrix[i+2][j+1]]
                    self.matrix.append(block)
                    block = []
               for i in range(3, self.rowSize, 2):
                    j = 0
                    block = [matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]]
                    self.matrix.append(block)
                    block = []
                    for j in range(3, self.columnSize, 2):
                         block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
                         self.matrix.append(block)
                         block = []

          # row:even column:odd
          if (isEven(self.rowSize)) and (not isEven(self.columnSize)):
               for i in range(0, self.rowSize, 2):
                    j = 0
                    block = [matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]]
                    self.matrix.append(block)
                    block = []
                    for j in range(3, self.columnSize, 2):
                         block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
                         self.matrix.append(block)
                         block = []

          # row:odd column:even
          if (not isEven(self.rowSize)) and (isEven(self.columnSize)):
               i = 0
               for j in range(0, self.columnSize, 2):
                    block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1], matrix[i+2][j], matrix[i+2][j+1]]
                    self.matrix.append(block)
                    block = []
               for i in range(3, self.rowSize, 2):
                    for j in range(0, self.columnSize, 2):
                         block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
                         self.matrix.append(block)
                         block = []

          # row:even column:even
          if (isEven(self.rowSize)) and (isEven(self.columnSize)):  
               for i in range(0, self.rowSize, 2):
                    for j in range(0, self.columnSize, 2):
                         block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
                         self.matrix.append(block)
                         block = []

     def getCell(self, x, y):
          pass
          
     def giveMatrix(self):
          return self.matrix
    

def isEven(num):
     if num%2==0:
          return True
     else:
          return False
     

blocky_major = MatrixBlocky([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ])
print(blocky_major.giveMatrix())