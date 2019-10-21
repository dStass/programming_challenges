'''
You are given a stream of numbers.
Compute the median for each new element.

Eg. Given [2, 1, 4, 7, 2, 0, 5],
the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
'''
import math
from blist import blist

# def running_median(stream):
#   if not stream or len(stream) == 0:
#     return None

#   sorted_list = blist([])
#   for i in range(0, len(stream)):
#     sorted_list.i


#   return running_median_sorted(stream)

def running_median_sorted(stream):
  if len(stream) < 2:
    return None

  to_return = []
  for i in range(0, len(stream)-1):
    index = 0.5*(i+1)
    if index % 1 == 0:
      to_return.append(stream[int(index)])
    else:
      to_return.append((stream[math.floor(index)] + stream[math.floor(index+1)])/2) 

  return to_return


print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2

print(running_median([0,1,2,3,4,5,6,7,8]))

