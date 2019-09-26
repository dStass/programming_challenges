'''
Problem: Buddy Strings
From: Coding Interview Pro 25/09/2019

Given two strings A and B of lowercase letters,
return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
'''

# Store all seen characters
# count number of differences between each string
# return True for cases:
# 2 differences and each index are swappable
# 0 differences AND a character is repeated (which means one of these
# occurrences can be swapped)
class Solution:
  def buddyStrings(self, A, B):
    if len(A) != len(B):
      return False
    
    if len(A) < 2:
      return False
    
    differences = 0
    d1 = None
    d2 = None
    seen = {}
    repeated = False
    for i in range(len(A)):
      if not repeated and seen.get(A[i], False):
        repeated = True
      else:
        seen[A[i]] = True

      if A[i] != B[i]:
        differences += 1
        if d1 != None:
          d2 = i
        else:
          d1 = i
      
      
      if differences > 2:
        return False
    
    if differences == 0 and repeated:
      return True

    if differences != 2:
      return False
    
    if A[d1] == B[d2] and A[d2] == B[d1]:
      return True
    return False

print(Solution().buddyStrings('a', 'a'))
print(Solution().buddyStrings('ab', 'ba'))
print(Solution().buddyStrings('ab', 'ab'))
print(Solution().buddyStrings('aa', 'aa'))
print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
