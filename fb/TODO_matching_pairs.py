'''
Matching Pairs

Given two strings s and t of length N,
find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively.
The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.

Signature
int matchingPairs(String s, String t)

Input
s and t are strings of length N
N is between 1 and 1,000,000
Output
Return an integer denoting the maximum number of matching pairs

Example
s = "abcd"
t = "adcb"
output = 4

Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
'''


import math
# Add any extra import statements you may need here

# Add any helper functions you may need here
def get_max_char_count(s_dict):
  max_count = 0
  for s in s_dict:
    s_count = s_dict.get(s)
    max_count = max(max_count, len(s_count))
  return max_count


# naive solution
def matching_pairs(s, t):





# if s == t 
def matching_pairs(s, t):

  # case len(s) == 1:
  # how shoul d we handle
  

  # case s == t: (or different = 0)
  # either return len(s) or len(s) - 2
  # case len(s) - 2: if all letters are unique
  # otherwise (ie at least one character which has a double)
  # then we can swap the double and preserve the same string
  # so we return len(s)

  # case when dif = 1:
  # ie [abcd,abce] or [abcc, abce]
  # if the character with mismatch is unique, we will have to swap two out of place
  # so we will swap it with another, ie 2 out of place
  # ret len(s) - 2
  # IF the singular mixmatch char is not unique,
  # we can swap it with another location of the same character
  # return len(s) - 1
  
  # case when dif = 2:
  # when you swap these, we will get either: 2 differences, 1 difference or 0 differences
  # 0 differences when s[i] = t[j] and s[j] = t[i]
  # 1 difference when s[i] = t[j] but s[j] != t[i]
  # 2 differences when s[i] != t[j] and s[j] != t[i]


  # case when dif > 2, ie 3, 4, 5, 6 . . .
  # abcdef bacfed
  # best case scenario when we swap 2
  # we get some s[i] == t[j] and s[j] == t[i]

  s_locations = {}  # holds unique chars to their own dicts
  # each subdict will contain key-value pairs: key(index in s) and value(bool)

  t_locations = {}


  num_differences = 0

  location_differences = []


  # we know len(s) == len(t)
  for i in range(len(s)):
    s_char = s[i]
    t_char = t[i]
    if s_char != t_char:
      num_differences += 1
      location_differences.append(i)


    
    s_char_dict = s_locations.get(s_char, {})
    s_char_dict[i] = True
    s_locations[s_char] = s_char_dict

    t_char_dict = t_locations.get(t_char, {})
    t_char_dict[i] = True
    t_locations[s_char] = t_char_dict

  


  max_matches = len(s)

  for difference_index in location_differences:
    s_char = s[difference_index]
    t_char = t[difference_index]

    s_char_locs = s_char_dict[s_char]
    t_char_locs = t_char_dict[t_char]

  print(s_locations, t_locations, num_differences)

  return max_matches


	# Write your code here
	











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
	n_1, s_1, t_1 = 5, "abcde", "adcbe"
	expected_1 = 5
	output_1 = matching_pairs(s_1, t_1)
	check(expected_1, output_1)

	s_2, t_2 = "abcd", "abcd"
	expected_2 = 2
	output_2 = matching_pairs(s_2, t_2)
	check(expected_2, output_2)

	# Add your own test cases here