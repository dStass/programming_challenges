'''
Balanced Split
Given a set of integers (which may include repeated integers),
determine if there's a way to split the set into two subsets
A and B such that the sum of the integers in both sets is the same,
and all of the integers in A are strictly smaller than all of the integers in B.

Signature
bool balancedSplitExists(int[] arr)

Input
All integers in array are in the range [0, 1,000,000,000].

Output
Return true if such a split is possible, and false otherwise.

Example 1
arr = [1, 5, 7, 1]
output = true
We can split the set into A = {1, 1, 5} and B = {7}.

Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the set into A = {6, 6, 7} and B = {7, 12}
since this doesn't satisfy the requirement that all integers in A are smaller than all integers in B.
'''

import math
# Add any extra import statements you may need here

# Add any helper functions you may need here

def balancedSplitExists(arr):

	# Write your code here
  arr = sorted(arr) # O(N * log(N))
  sum_left = 0
  length_left = 0
  length_right = len(arr)
  sum_right = sum(arr) # O(N)

  split_index = 0
  # left set from [0->split_index), right from split_index ->
  while sum_left <= sum_right:  # O(N)
    if sum_left == sum_right and length_left != 0 and length_right != 0:
      return True
    
    if split_index == len(arr):
      break

    split_val = arr[split_index]
    while arr[split_index] == split_val:
      sum_left += arr[split_index]
      sum_right -= arr[split_index]
      
      length_left += 1
      length_right -= 1

      split_index += 1
      if split_index == len(arr):
        break

  # Total complexity: O(N * log(N)) + 2*O(N) ==> O(N * log(N))

  return False









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
	print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # 3
  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)
 

  # Add your own test cases here
  # 4
  arr_2 = [2, 2, 2, 2, 2, 5, 5]
  expected_2 = True
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  # 5
  arr_2 = [2, 2, 2, 2, 0, 5, 3]
  expected_2 = True
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # 6
  arr_2 = [2, 2, 2, 2, 3, 5, 5]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)


  # 7
  arr_2 = [0, 0, 0, 0]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)


  # 7
  arr_2 = [0, 1, 1, 2]
  expected_2 = True
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

