'''
Problem: Room Scheduling 12/10/2019

You are given an array of tuples (start, end)
representing time intervals for lectures.
The intervals may be overlapping.
Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2
'''

def min_rooms(intervals):
  if len(intervals) < 1:
    return 0

  start = intervals[0][0]
  end = intervals[0][1]

  for interval in intervals:
    if interval[0] < start:
      start = interval[0]
    if interval[1] > end:
      end = interval[1]
  
  print("range=", end-start)
  return 2

(min_rooms([(30, 75), (15, 50), (60, 150)]))
