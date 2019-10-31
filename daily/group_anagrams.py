'''
Problem: Group Words That are Anagrams
From: Daily Interview Pro 10/10/2019

Given a list of words, group the words that are anagrams of each other.
(An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
'''

def groupAnagramWords(strs):
  existing_anagrams = {}
  for s in strs:
    s_sorted = ''.join(sorted(s))
    a = existing_anagrams.get(s_sorted, [])
    a.append(s)
    existing_anagrams[s_sorted] = a
  
  to_return = []
  for e in existing_anagrams:
    to_return.append(existing_anagrams[e])
  return to_return[::-1]


print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg', 'max', 'xam', 'earth', 'heart']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
