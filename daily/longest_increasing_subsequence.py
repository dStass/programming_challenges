'''
You are given an array of integers.
Return the length of the longest increasing subsequence
(not necessarily contiguous) in the array. 

Example:
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

The following input should return 6 since the longest
increasing subsequence is 0, 2, 6, 9 , 11, 15.
'''

# O(N^2) Solution
def longest(arr):
  if len(arr) == 0:
    return 0
  
  # array containing longest sub-sequence so far
  longest_sub = [0] * len(arr)
  for i in range(len(arr)):
    best = 0
    for j in range(i):
      if arr[i] > arr[j] and best < longest_sub[j]:
        best = longest_sub[j]
    longest_sub[i] = best + 1
  return longest_sub[-1]

print(longest([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))  # 6

print(longest([1]))  # 1
print(longest([]))  # 0
print(longest([6,5,4,3,2,1,0]))  # 1 - descending list, therefore longest = any number
