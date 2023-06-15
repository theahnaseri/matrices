from MatrixRowMajor import MatrixRowMajor
from MatrixColumnMajor import MatrixColumnMajor
from MatrixBlocky import MatrixBlocky


_matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
x = 1
y = 0
print('------------------------------')
print('matrix :', _matrix)
print('------------------------------')

row_major = MatrixRowMajor(_matrix)
row_major_matrix = row_major.giveMatrix()
row_major_element = row_major.getCell(x, y)
print('row-major representation :', row_major_matrix)
print('row-major element :', row_major_element)
print('------------------------------')

column_major = MatrixColumnMajor(_matrix)
column_major_matrix = column_major.giveMatrix()
column_major_element = column_major.getCell(x, y)
print('column-major representation :', column_major_matrix)
print('column-major element :', column_major_element)
print('------------------------------')

blocky_major = MatrixBlocky(_matrix)
blocky_matrix = blocky_major.giveMatrix()
blocky_element = blocky_major.getCell(x, y)
print('blocky representation :', blocky_matrix)
print('blocky element :', blocky_element)
print('------------------------------')

assert (_matrix[x][y]==row_major_element) and (_matrix[x][y]==column_major_element) and (_matrix[x][y]==blocky_element)

# example
# [ [1, 2], [3, 4] ]
# [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
# [ [1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48], [49, 50, 51, 52, 53, 54, 55, 56], [57, 58, 59, 60, 61, 62, 63, 64], [65, 66, 67, 68, 69, 70, 71, 72], [73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88], [89, 90, 91, 92, 93, 94, 95, 96] ]