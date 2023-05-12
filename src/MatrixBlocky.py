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
          block = getBlock(self.rowSize, self.columnSize, x, y)
          element = getElement(self.rowSize, self.columnSize, x, y)
          return self.matrix[block][element]
          
     def giveMatrix(self):
          return self.matrix
    

def isEven(num):
     if num%2==0:
          return True
     else:
          return False
     
def getElement(rowSize, columnSize, matrixRow, matrixColumn):
     # row:odd column:odd
     if (not isEven(rowSize)) and (not isEven(columnSize)):
          if matrixRow==0:
               if matrixColumn==0:
                    element = 0
               elif matrixColumn==1:
                    element = 1
               elif matrixColumn==2:
                    element = 2
               elif not isEven(matrixColumn):
                    element = 0
               elif isEven(matrixColumn):
                    element = 1

          elif matrixRow==1:
               if matrixColumn==0:
                    element = 3
               elif matrixColumn==1:
                    element = 4
               elif matrixColumn==2:
                    element = 5
               elif not isEven(matrixColumn):
                    element = 2
               elif isEven(matrixColumn):
                    element = 3

          elif matrixRow==2:
               if matrixColumn==0:
                    element = 6
               elif matrixColumn==1:
                    element = 7
               elif matrixColumn==2:
                    element = 8
               elif not isEven(matrixColumn):
                    element = 4
               elif isEven(matrixColumn):
                    element = 5

          elif not isEven(matrixRow):
               if matrixColumn==0:
                    element = 0
               elif matrixColumn==1:
                    element = 1
               elif matrixColumn==2:
                    element = 2
               elif not isEven(matrixColumn):
                    element = 0
               elif isEven(matrixColumn):
                    element = 1

          elif isEven(matrixRow):
               if matrixColumn==0:
                    element = 3
               elif matrixColumn==1:
                    element = 4
               elif matrixColumn==2:
                    element = 5
               elif not isEven(matrixColumn):
                    element = 2
               elif isEven(matrixColumn):
                    element = 3

     # row:even column:odd
     elif (isEven(rowSize)) and (not isEven(columnSize)):
          if matrixColumn==0:
               if isEven(matrixRow):
                    element = 0
               else:
                    element = 3
          elif matrixColumn==1:
               if isEven(matrixRow):
                    element = 1
               else:
                    element = 4
          elif matrixColumn==2:
               if isEven(matrixRow):
                    element = 2
               else:
                    element = 5
          else:
               if (isEven(matrixRow)) and (not isEven(matrixColumn)):
                    element = 0
               elif (isEven(matrixRow)) and (isEven(matrixColumn)):
                    element = 1
               elif (not isEven(matrixRow)) and (not isEven(matrixColumn)):
                    element = 2
               elif (not isEven(matrixRow)) and (isEven(matrixColumn)):
                    element = 3

     # row:odd column:even
     elif (not isEven(rowSize)) and (isEven(columnSize)):
          if matrixRow==0:
               if isEven(matrixColumn):
                    element = 0
               else:
                    element = 1
          elif matrixRow==1:
               if isEven(matrixColumn):
                    element = 2
               else:
                    element = 3
          elif matrixRow==2:
               if isEven(matrixColumn):
                    element = 4
               else:
                    element = 5
          else:
               if (not isEven(matrixRow)) and (isEven(matrixColumn)):
                    element = 0
               elif (not isEven(matrixRow)) and (not isEven(matrixColumn)):
                    element = 1
               elif (isEven(matrixRow)) and (isEven(matrixColumn)):
                    element = 2
               elif (isEven(matrixRow)) and (not isEven(matrixColumn)):
                    element = 3

     # row:even column:even
     elif (isEven(rowSize)) and (isEven(columnSize)):
          if (isEven(matrixRow)) and (isEven(matrixColumn)):
               element = 0
          elif (isEven(matrixRow)) and (not isEven(matrixColumn)):
               element = 1
          elif (not isEven(matrixRow)) and (isEven(matrixColumn)):
               element = 2
          elif (not isEven(matrixRow)) and (not isEven(matrixColumn)):
               element = 3
     
     return element
          

def getBlock(rowSize, columnSize, matrixRow, matrixColumn):
     # row:odd column:odd
     if (not isEven(rowSize)) and (not isEven(columnSize)):
          if matrixRow==0 or matrixRow==1 or matrixRow==2:
               blockRow = 0
          else:
               blockRow = (matrixRow-1)//2
          if matrixColumn==0 or matrixColumn==1 or matrixColumn==2:
               blockColumn = 0
          else:
               blockColumn = (matrixColumn-1)//2

     # row:even column:odd
     elif (isEven(rowSize)) and (not isEven(columnSize)):
          blockRow = matrixRow//2
          if matrixColumn==0 or matrixColumn==1 or matrixColumn==2:
               blockColumn = 0
          else:
               blockColumn = (matrixColumn-1)//2

     # row:odd column:even
     elif (not isEven(rowSize)) and (isEven(columnSize)):
          if matrixRow==0 or matrixRow==1 or matrixRow==2:
               blockRow = 0
          else:
               blockRow = (matrixRow-1)//2
          blockColumn = matrixColumn//2

     # row:even column:even
     elif (isEven(rowSize)) and (isEven(columnSize)):
          blockRow = matrixRow//2
          blockColumn = matrixColumn//2

     block = (blockRow)*(columnSize//2) + blockColumn

     return block  