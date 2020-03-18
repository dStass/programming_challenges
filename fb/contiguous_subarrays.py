'''
Contiguous Subarrays
You are given an array a of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfills the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end with i.
Signature
int[] countSubarrays(int[] arr)
Input
Array a is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of a[i]
Example:
a = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]

Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 -[1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
'''



import math



def count_subarrays(arr):
  # naive approach:
  to_return = [1] * len(arr)
  for i, i_val in enumerate(arr):
    j = i + 1
    while(j < len(arr)):
      j_val = arr[j]
      if j_val > i_val:
        break
      j += 1
      to_return[i] += 1

    j = i - 1
    while (j >= 0):
      j_val = arr[j]
      if j_val > i_val:
        break
      j -= 1
      to_return[i] += 1
  
  return to_return









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
	print('[', n, ']', sep='', end='')

def printIntegerList(array):
	size = len(array)
	print('[', end='')
	for i in range(size):
		if i != 0:
			print(', ', end='')
		print(array[i], end='')
	print(']', end='')

test_case_number = 1

def check(expected, output):
	global test_case_number
	expected_size = len(expected)
	output_size = len(output)
	result = True
	if expected_size != output_size:
		result = False
	for i in range(min(expected_size, output_size)):
		result &= (output[i] == expected[i])
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printIntegerList(expected)
		print(' Your output: ', end='')
		printIntegerList(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
	test_1 = [3, 4, 1, 6, 2]
	expected_1 = [1, 3, 1, 5, 1]
	output_1 = count_subarrays(test_1)
	check(expected_1, output_1)

	test_2 = [2, 4, 7, 1, 5, 3]
	expected_2 = [1, 2, 6, 1, 3, 1]
	output_2 = count_subarrays(test_2)
	check(expected_2, output_2)


