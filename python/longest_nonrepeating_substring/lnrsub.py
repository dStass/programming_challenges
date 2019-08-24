'''
From: Daily Interview Pro 18/08/2019
Problem: Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
Can you find a solution in linear time?
'''

class Solution:

  # Solution will return first occurence of max length substring
  def lengthOfLongestSubstring(self, s):
    longest = ""  # longest found non-repeating substring
    so_far = ""  # non-repeating substring so far
    for c in s:
      if c not in so_far:  # if c is a non-repeating character
        so_far += c  # add it to current string
        if len(so_far) > len(longest):  # if current substring is longer than previous longest
          longest = so_far  # set longest to so_far
      else:
        so_far = "" + c  # if c IS repeated, start current sub_string again with JUST that char
    return len(longest)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
print(Solution().lengthOfLongestSubstring('abcdefghaijklfghijklmnooo'))

# 10
