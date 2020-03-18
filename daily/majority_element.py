# A majority element is an element that appears more than half the time. Given a list with a majority element, find the majority element.



def majority_element(nums):
  num_freq = {}
  for n in nums:
    num_freq[n] = num_freq.get(n, 0) + 1
  
  num_items = len(nums)

  to_return = None
  for n in num_freq:
    f = num_freq[n]
    if f > num_items / 2:
      to_return = n
      break
  
  return to_return

print(majority_element([3, 5, 5, 5, 5, 5,5,5,5,3, 3, 2, 4, 3]))
# 3

print(majority_element([1,3,2,2]))
