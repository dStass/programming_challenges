'''
From: Daily Interview Pro 18/08/2019
Problem: Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
Can you find a solution in linear time?
'''

class Solution:

  # Solution will return first occurence of max length substring
  def lengthOfLongestSubstring(self, s):
    longest = 0  # max len
    so_far = 0  # non-repeating len so far
    last_visited = {}  # stores location of last visited
    index = 0

    last_visited[s[0]] = 0
    for c in s:
      if index == 0:
        index += 1
        continue

      index += 1
      prev_c = last_visited.get(c)
      if prev_c == None or index - so_far > prev_c:
        so_far += 1
      else:
        if so_far > longest:
          longest = so_far
        so_far = index - prev_c
      last_visited[c] = index

    # final check for so_far reaching end of string
    if so_far > longest:
      longest = so_far
    return longest


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
print(Solution().lengthOfLongestSubstring('abcdefghijalmno'))