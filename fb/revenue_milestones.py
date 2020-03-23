'''
Revenue Milestones

We keep track of the revenue Facebook makes every day,
and we want to know on what days Facebook hits certain revenue milestones.
Given an array of the revenue on each day, and an array of milestones Facebook wants to reach,
return an array containing the days on which Facebook reached every milestone.

Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)

Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N).
milestones is a length-K array of interesting total revenue milestones.

Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue.

Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]

Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively.
Day 6 is the first time that FB has >= $200 of total revenue.
'''

import math
# Add any extra import statements you may need here

# Add any helper functions you may need here

def getMilestoneDays(revenues, milestones):
  running_sum = 0
  milestones_tuples = []
  for index, milestone in enumerate(milestones):
    milestones_tuples.append((milestone, index))
  milestones_tuples = sorted(milestones_tuples)

  to_return = []
  milestone_index = 0
  milestones_hit = []

  current_milestone = milestones_tuples[0][0]

  for day, r in enumerate(revenues):
    running_sum += r

    if milestone_index == len(milestones_tuples):
      break
    while running_sum >= current_milestone:
      milestones_hit.append((milestones_tuples[milestone_index][1], day + 1))
      milestone_index += 1
      if milestone_index == len(milestones_tuples):
        break
      current_milestone = milestones_tuples[milestone_index][0]

  milestones_hit = sorted(milestones_hit)
  print(milestones_hit)
  for milestones_pair in milestones_hit:
    to_return.append(milestones_pair[1])

  return to_return
  
  
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

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
	revenues_1 = [100, 200, 300, 400, 500]
	milestones_1 = [300, 800, 1000, 1400]
	expected_1 = [2, 4, 4, 5]
	output_1 = getMilestoneDays(revenues_1, milestones_1)
	check(expected_1, output_1)

	revenues_2 = [700, 800, 600, 400, 600, 700]
	milestones_2 = [3100, 2200, 800, 2100, 1000] 
	expected_2 = [5, 4, 2, 3, 3]
	output_2 = getMilestoneDays(revenues_2, milestones_2)
	check(expected_2, output_2)


	# Add your own test cases here