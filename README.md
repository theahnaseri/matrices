# matrices
There are three methods of storing the matrix, which we will explain each one:

In Matrix Row Major storage, the elements of a matrix are stored in a contiguous block of memory row by row.
Row major storage is efficient for accessing consecutive elements along a row, since they are stored contiguously in memory. However, accessing elements along a column requires skipping over several memory locations, which can result in cache misses and slower performance.

In Matrix Column Major storage, the elements of a matrix are stored in a contiguous block of memory column by column.
Column major storage is efficient for accessing consecutive elements along a column, since they are stored contiguously in memory. However, accessing elements along a row requires skipping over several memory locations, which can result in cache misses and slower performance.

Matrix Blocky storage is a variant of matrix storage where the matrix is divided into smaller blocks of equal size, and each block is stored contiguously in memory.
In Matrix Blocky storage, the matrix is partitioned into a set of non-overlapping submatrices or blocks. Each block is usually rectangular and has a fixed size. The blocks are stored in a one-dimensional array in row-major order, that is, the blocks in the first row of the matrix are stored sequentially, followed by the blocks in the second row, and so on.
Matrix Blocky storage can be useful for certain algorithms such as matrix multiplication, where the computation can be performed on blocks of the matrices rather than on individual elements. This can reduce cache misses and improve performance.
