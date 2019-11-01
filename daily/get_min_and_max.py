'''
Problem: Max and Min with Limited Number of Comparisons
From: Daily Interview pro 31/10/2019

Given a list of numbers of size n, where n is greater than 3,
find the maximum and minimum of the list
using less than 2 * (n - 1)comparisons.
'''

class MinMax:
  comps = 0
  def find_min_max(self, nums, get_max=True, get_min=True):
    small_list = []
    large_list = []
    self.comps += 1
    if len(nums) == 0:
      return None
    self.comps += 1
    if len(nums) == 1:
      return [nums[0], nums[0]]

    end = len(nums)
    self.comps += 1
    if len(nums) % 2 == 1:  # even case
      end -= 1

    for i in range(0, end, 2):
      pair = [nums[i], nums[i+1]]
      larger_pos = self.larger_position(pair)
      large_list.append(pair[larger_pos])
      small_list.append(pair[1-larger_pos])


    maximum = 0
    minimum = 0
    self.comps += 2
    if get_max:
      maximum = self.find_min_max(large_list, get_min=False)[1]
    if get_min:
      minimum = self.find_min_max(small_list, get_max=False)[0]
    
    self.comps += 3
    if len(nums) % 2 == 1:
      if nums[end] > maximum:
        maximum = nums[end]
      if nums[end] < minimum:
        minimum = nums[end]


    return [minimum, maximum]


  def larger_position(self, pair):  # returns 0 or 1
    self.comps += 1
    if pair[0] > pair[1]:
      return 0
    else:
      return 1



mm = MinMax()

print(mm.find_min_max([3, 5, 1, 2, 4, 8]), mm.comps)
# (1, 8)

print(mm.find_min_max(range(8199)), mm.comps)