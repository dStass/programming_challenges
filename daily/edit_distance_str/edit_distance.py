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
  distance = []
  for i in range(num_rows):
    distance.append([0] * num_cols)

  for i in range(1, num_rows):
    for k in range(1, num_cols):
      distance[i][0] = i
      distance[0][k] = k
  
  for col in range(1, num_cols):
    for row in range(1, num_rows):
      if s1[row - 1] == s2[col - 1]:
        cost = 0
      else:
        cost = 1
      distance[row][col] =  min(distance[row - 1][col] + 1,
                            distance[row][col - 1] + 1,
                            distance[row - 1][col - 1] + cost)
  return distance[row][col]

print(distance('biting', 'sitting'))
# 2
