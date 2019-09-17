'''
Problem: Spiral Traversal of Grid
From: Coding Interview Pro 16/09/2019

You are given a 2D array of integers.
Print out the clockwise spiral traversal of the matrix.

Example:
grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
'''

def matrix_spiral_print(M):
  rows = len(M)
  if rows == 0:
    return
  cols = len(M[0])
  if cols == 0:
    return

  end_row = rows - 1
  end_col = cols - 1
  start_row = 0
  start_col = 0

  printed = 0
  total = rows * cols
  while (printed < total):

    # right
    for i in range(start_col, end_col):
      print(M[start_row][i], " ", end='')
      printed += 1
    start_col += 1

    # down
    for i in range(start_row, end_row):
      print(M[i][end_col - 1], " ", end='')
      printed += 1
    start_row += 1


  print()

# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]

grid = [[1,  2,  3,  4,  5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12



# plan
# n x m matrix:
# 3 x 3: 
# print 0,0 0,1 0,2 1,2 2,2 2,1 2,0, 1,0, 1,1
# 4x4: 
# print 0,0 0,1 0,2 0,3 1,3 2,3, 3,3 