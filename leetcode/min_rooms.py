'''
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''


class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    starts = []
    ends = []
    
    for i in intervals:
      starts.append(i[0])
      ends.append(i[1])
    
    starts.sort()
    ends.sort()
    
    start = 0
    end = 0
    rooms = 0
    while (start < len(intervals)):
      if starts[start] >= ends[end]:
        end += 1
      else:
        rooms += 1
      start += 1
    
    return rooms