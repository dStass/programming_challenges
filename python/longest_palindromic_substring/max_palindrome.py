'''
From: Daily Interview Pro 19/08/2019
Problem: Longest Palindromic Substring

A palindrome is a sequence of characters that reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.
'''
class Solution:
    def longestPalindrome(self, s):
      string_length = len(s)
      curr = 0
      for c in s:
        curr += 1
      return curr

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
