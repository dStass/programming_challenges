'''
Problem: Merge Overlapping Intervals
From: Coding Interview Pro 18/09/2019

You are given an array of intervals - that is,
an array of tuples(start, end).
The array may not be sorted, and could contain overlapping intervals.
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)]
since (5, 8) and (4, 10) can be merged into (4, 10).
'''

def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # First we sort intervals
  intervals.sort()
  curr_index = 1
  while (curr_index < len(intervals)):
    prev = intervals[curr_index - 1]
    curr = intervals[curr_index]
    if can_be_merged(prev, curr):

      # if two intervals can be merged, set curr to the merged interval
      # and delete the previous one
      intervals[curr_index] = merge_intervals(prev, curr)
      curr_index -= 1
      del intervals[curr_index]
    curr_index += 1
  return intervals

# two ways to merge: 
def can_be_merged(i1, i2):
  # engulfed case where i2 is contained inside i1 wholly
  if i2[0] >= i1[0] and i2[1] <= i1[1]:
    return True

  # overlap case 1 where the end of the first interval is
  # between the start and end of the second interval
  elif i1[0] <= i2[0] and i1[1] >= i2[0] and i1[1] <= i2[1]:
    return True

  return False

def merge_intervals(i1, i2):
  first = min(i1[0], i2[0])
  second = max(i1[1], i2[1])
  to_return = (first, second)
  return to_return
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]


# tests overlap case 2
print(merge([(1, 3), (2, 5), (20, 25)]))
# [(1, 5), (20, 25)]

# tests overlap case 1
print(merge([(1, 3), (2, 5), (20, 25)]))
# [(1, 5), (20, 25)]

# tests non-overlap adjacent intervals
print(merge([(1, 2), (3, 5), (20, 25)]))
# [(1, 5), (20, 25)]

print(merge([(1, 3), (2, 6), (8, 10), (15,18)]))