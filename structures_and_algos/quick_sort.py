"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
  pivots = list(range(len(array)))
  from_stack = []
  to_stack = []

  from_stack.append(0)
  to_stack.append(len(array) - 1)
  while pivots:
    pivot = pivots.pop()
    fr = from_stack.pop()
    to = to_stack.pop()
    


  return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))