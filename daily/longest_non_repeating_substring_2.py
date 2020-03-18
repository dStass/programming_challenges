'''
From: Daily Interview Pro 18/08/2019
Problem: Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
Can you find a solution in linear time?
'''
class Solution:
  def lengthOfLongestSubstring(self, s):
    if len(s) in [0,1]:
        return len(s)

    max_len = 1
    curr_len = 1
    start = 0
    end = 0

    letter_count = {}
    letter_count[s[start]] = 1

    while start < len(s): 
      end += 1
      if end == len(s):  # end traverses at most n indices
        break

      end_char = s[end] # O(1)
      letter_count[end_char] = letter_count.get(end_char, 0) + 1 # O(1)
      char_count = letter_count[end_char] # O(1)


      # loops while the end's character count is 2 (ie > 1)
      # for a non-repeating substring, ALL character should have a 
      # count of 1
      while char_count > 1: # start traverses at max from index 0 to index n

        # all O(1) below
        # increase start index by 1 and decrease the character located there by 1
        start_char = s[start]
        letter_count[start_char] = letter_count[start_char] - 1
        start += 1

        # reset loop - char_count = count for character at end index so far in substring
        char_count = letter_count[end_char]

      curr_len = end - start + 1
      max_len = max(max_len, curr_len)

    return max_len


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
print(Solution().lengthOfLongestSubstring('abcdefaaghijaalmno'))