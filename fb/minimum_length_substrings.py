'''
Minimum Length Substrings
You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
Signature
int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"'
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
'''

import math
# Add any extra import statements you may need here



# Add any helper functions you may need here

# const time: only maximum 26 characters in dict
def is_substring(small, large):
  for s_char in small:
    if small[s_char] > large.get(s_char, 0):
      return False
  
  return True


def min_length_substring(s, t):
	# Write your code here
    if len(s) < len(t):
      return -1
    
    min_solution = -1
    
    t_dict = {}
    for t_char in t:
      t_dict[t_char] = t_dict.get(t_char, 0) + 1
    
    minimum_length = len(t)
    
    
    s_dict = {}
    for s_char in s[:minimum_length]:
      s_dict[s_char] = s_dict.get(s_char, 0) + 1

    start = 0
    end = minimum_length
    
    while end < len(s) - 1:

      while end-start + 1 >= len(t) and is_substring(t_dict, s_dict):
        substring_length = end - start + 1
        if min_solution == -1:
          min_solution = end - start + 1
        else:
          min_solution = min(min_solution, substring_length)
        start_char = s[start]
        s_dict[start_char] = s_dict.get(start_char, 0) - 1
        start += 1
        # print(s[start:end+1])

      end += 1
      end_char = s[end]
      s_dict[end_char] = s_dict.get(end_char, 0) + 1
    
    return min_solution
      



      
    
	











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
	print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printInteger(expected)
		print(' Your output: ', end='')
		printInteger(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
	s1 = "dcbefebce"
	t1 = "fd"
	expected_1 = 5
	output_1 = min_length_substring(s1, t1)
	check(expected_1, output_1)

	s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
	t2 = "cbccfafebccdccebdd"
	expected_2 = -1
	output_2 = min_length_substring(s2, t2)
	check(expected_2, output_2)

	# Add your own test cases here