'''
There are n people lined up, and each have a height represented as an integer.
A murder has happened right in front of them, and only people who are taller
than everyone in front of them are able to see what has happened.
How many witnesses are there?

Example:
Input: [3, 6, 3, 4, 1]  
Output: 3
Explanation: Only [6, 4, 1] were able to see in front of them.
 #
 #
 # #
####
####
#####
36341                                 x (murder scene)
'''

# traverse list backwards
# if value at index larger than max, update max
# increment count and return at the end
def witnesses(heights):
  count = 0
  tallest = 0
  for i in range(len(heights) - 1, -1, -1):
    if heights[i] > tallest:
      count += 1
      tallest = heights[i]
  return count

print(witnesses([3, 6, 3, 4, 1]))
# 3
print(witnesses([8,7,6,5,4,9,2,1]))

