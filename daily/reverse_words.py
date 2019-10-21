'''
Problem: Reverse a Words in a String
From: Coding Interview Pro 13/10/2019

Given a string, you need to reverse the order of characters
in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space
and there will not be any extra space in the string.
'''

class Solution:
  def reverseWords(self, str):
    new_str = ""
    str_split = str.split()
    for s in str_split:
      s_reverse = s[::-1]
      new_str += s_reverse + " "
    return new_str.strip()

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
