'''
From: Coding Interview Pro 07/09/2019
Problem: Number of ways to traverse a grid

You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.
'''

# n horizontal grids
# m vertical grids
# (n-1) "arrows/paths" between each horizontal grid
# Similarly m-1 for vertical
# Permutation problem
# total amount of ways (n-1) + (m-1)
# divided by (n-1)! ways, div again by (m-1)! possible ways
# as each vertical/horizontal paths are not unique
def num_ways(n, m):
  factorials = [0] * (n+m-1)
  factorials[0] = 1
  for i in range(1, n+m-1):
    factorials[i] = i * factorials[i-1]
  num_ways = factorials[n+m-2] / (factorials[n-1]*factorials[m-1])
  return int(num_ways)

def num_ways_spop(n, m):
  # space optimised
  n_m_ways = 0
  n_ways = 0
  m_ways = 0
  i_factorial = 1
  for i in range(1, n+m-1):
    i_factorial *= i
    if i == n+m-2:
      n_m_ways = i_factorial
    if i == n-1:
      n_ways = i_factorial
    if i == m-1:
      m_ways = i_factorial
  return int(n_m_ways / (n_ways * m_ways))



print(num_ways(4, 4))
# 2
