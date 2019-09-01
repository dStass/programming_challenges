'''
From: Coding Interview Pro 01/09/2019
Problem: Edit Distance

Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits
(insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2
(substitute b for s, and insert a t).
'''

# edit distance defined as number of different chars
# INSERTION, DELETION AND SUBSTIITUTION
# use Levenshtein distance
def distance(s1, s2):
  num_rows = len(s1) + 1
  num_cols = len(s2) + 1

  # Create a zero matrix len(s1) + 1 x len(s2) + 1
  # We plus one to include "base case" subproblem ''
  distance = []
  for i in range(num_rows):
    distance.append([0] * num_cols)

  for i in range(1, num_rows):
    distance[i][0] = i
  
  for k in range(1, num_cols):
    distance[0][k] = k
  
  # Make matrix: 
  # '' denotes empty str
  #
  #    '' k0 k2 . . .  kn 
  # '' 0  1  2  3 . . . k
  # i0 1
  # i1 2
  # i2 3
  # .  .
  # .  .
  # .  .
  # in i


  for col in range(1, num_cols):
    for row in range(1, num_rows):
      cost = 0 if s1[row - 1] == s2[col - 1] else 1  # no substitution necessary if same char
      distance[row][col] =  min(distance[row - 1][col] + 1,  # deletions
                            distance[row][col - 1] + 1,  # insertions
                            distance[row - 1][col - 1] + cost)  # substitution
      print_matrix(distance)
  return distance[row][col]

def print_matrix(matrix):
  for row in matrix:
    print(row)
  print("\n")

print(distance('david', 'wave'))
print(distance('biting', 'sitting'))
# 2
