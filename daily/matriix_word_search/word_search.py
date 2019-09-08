'''
From: Coding Interview Pro 05/09/2017
Problem: Word Search

You are given a 2D array of characters, and a target string.
Return whether or not the word target word exists in the matrix.
Unlike a standard word search, the word must be either going left-to-right,
or top-to-bottom in the matrix.

Example:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true,
as it can be found going up-to-down in the first column.
'''


# Assumptions:
# Sqare matrix
# first load matrix into hash map between each char and
# its location in the matrix
def word_search(matrix, word):
  wsize = len(word)
  msize = len(matrix)
  if wsize > msize or wsize == 0:
    return False

  starting_with = {}
  for row in range(msize):
    for col in range(msize):
     char_here = matrix[row][col]
     coord_here = [row, col]
     chars_at = starting_with.get(char_here, [])
     chars_at.append(coord_here)
     starting_with[char_here] = chars_at
  
  first_char = word[0]
  start_locs = starting_with.get(first_char, [])
  for coords in start_locs:
    row = coords[0]
    col = coords[1]

    # check horizontal
    if col + wsize <= msize:
      to_compare = get_horizontal(matrix, coords, wsize)
      if to_compare == word:
        return True
    
    # check vertical
    if row + wsize <= msize:
      to_compare = get_vertical(matrix, coords, wsize)
      if to_compare == word:
        return True
  # checked all starting coordinates
  return False

def get_horizontal(matrix, coords, size):
  to_return = ""
  for i in range(size):
    to_return += matrix[coords[0]][coords[1] + i]
  return to_return

def get_vertical(matrix, coords, size):
  to_return = ""
  for i in range(size):
    to_return += matrix[coords[0] + i][coords[1]]
  return to_return

  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'ANOP'))
# True
