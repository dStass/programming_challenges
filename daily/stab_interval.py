# Let X be a set of n intervals on the real line.
# We say that a set of points P "stabs" X if every interval in X contains at least one point in P.
# Compute the smallest set of points that stabs X.
# For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].




# Explanation:
#
# 
# traverse sorted list from left to right, 
# pick the first END point (ie pick min_end)
# this is the start of our interval
# similarly pick the max_start value to end our interval
#
#
#                |--------------| - our smallest stab interval
#               (*) - min_end  (*) - max_start     
#       |--------|--|     |-----|--------|
# <--+--+--+--+--+--+--+--+--+--+--+--+--+--+-->
#    0  1  2  3  4  5  6  7  8  9 10 11 12 13
#  
# given (1,4), (4,5), (7,9), (9,12)
def smallest_stabbing_interval(intervals):
  if not intervals or len(intervals) < 1:
    return (None, None)
  
  intervals = sorted(intervals)

  min_end = intervals[0][1]
  max_start = intervals[0][0]
  for interval in intervals:
    interval_start = interval[0]
    interval_end = interval[1]
    min_end = min(min_end, interval_end)
    max_start = max(max_start, interval_start)

  # if max_start <= min_end ie our interval goes backwards
  # we can return a single point
  if max_start <= min_end:
    min_end = max_start
  return (min_end, max_start)


intervals = [(1,4), (4,5), (7,9), (9,12)]

print(smallest_stabbing_interval(intervals))