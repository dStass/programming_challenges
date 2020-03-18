'''
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is,
two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

Signature
int numberOfWays(int[] arr, int k)

Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].

Output
Return the number of different pairs of elements which sum to k.

Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.

Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
'''

import math
# Add any extra import statements you may need here

# Add any helper functions you may need here

def pair_in_arr(pair, array_length):
  for p in pair:
    # print(p, array_length)
    if p not in range(array_length):
      return False
  return True

def numberOfWays(arr, k):
 	# Write your code here

  arr = sorted(arr)
  array_length = len(arr)
  
  seen = {}
  queue = []

  num_ways = 0
  col = array_length - 1
  row = 0
  queue.append([col, row])


  while queue:
    pair = queue.pop(0)
    col = pair[0]
    row = pair[1]
    pair_sum = arr[col] + arr[row]

    seen[str(sorted(pair))] = True

    if pair_sum == k and row != col:
      num_ways += 1
      left_pair = [col-1, row]

      if pair_in_arr(left_pair, array_length) and str(sorted(left_pair)) not in seen:
        queue.append(left_pair)
  
    down_pair = [col, row+1]
    if pair_in_arr(down_pair, array_length) and str(sorted(down_pair)) not in seen:
      queue.append(down_pair)



  # while col >= 0 and row < array_length:
  #   pair = str(sorted([col, row]))
  #   if col == row:
  #     seen[pair] = True
  #   pair_sum = arr[col] + arr[row]
  #   if pair_sum == k and pair not in seen:
  #     print("[{},{}]".format(col, row))
  #     # print(pair)
  #     num_ways += 1
  #     col -= 1
  #     seen[pair] = True
  #     continue
  #   row += 1

  return num_ways











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
	k_1 = 6
	arr_1 = [1, 2, 3, 4, 3]
	expected_1 = 2
	output_1 = numberOfWays(arr_1, k_1)
	check(expected_1, output_1)

	k_2 = 6
	arr_2 = [1, 5, 3, 3, 3]
	expected_2 = 4
	output_2 = numberOfWays(arr_2, k_2)
	check(expected_2, output_2)

 	# Add your own test cases here