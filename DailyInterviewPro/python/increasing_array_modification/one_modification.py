'''
From Daily Interview Pro 26/08/2019
Problem: Non-Decreasing Array with Single Modification

You are given an array of integers in an arbitrary order.
Return whether or not it is possible to make the array non-decreasing
by modifyingat most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1]
holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less,
to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one
element to make the array non-decreasing.

'''


# O(N) algorithm
def check(lst):
  size = len(lst)
  modification_count = 0
  for i in range(1, size):
    if lst[i] < lst[i-1]:
      # two cases, either we have a valley
      # ie check prev and next and make sure they are in increasing order
      if i == size-1: # if last num
        return True if modification_count == 0 else False
      
      # check valley, make sure the next is not less than this
      if lst[i+1] < lst[i]:
        return False

      # check valley (check next is greater than or equal to previous)
      if lst[i+1] >= lst[i-1]:
        lst[i] = lst[i-1]
        modification_count += 1
      else:  # we know that next is less than prev but greater than curr, can we modify prev to make list increasing?
        # or the previous value is a peak
        if i == 1:  # check if prev is first value, if it is we can make one modification no problem
          lst[0] = lst[1]
          modification_count+=1
        else:  # interesting situtation where we have to check prevprev value
          if lst[i-2] <= lst[i]:  # check if 2 previous is -le to curr
            lst[i-1] = lst[i-2]  # if it is, we can make one modification to prev as it is a peak
            modification_count+=1
          else:
            return False

    if modification_count > 1:
      return False
  return True

  

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False


# tests:

print(check([1,2,3])) # true, increasing
print(check([1,3,5,7,6])) # true last item, one error
print(check([5,1,2,3,4])) # true first item, one error
print(check([2,4,6,5,6,6,8])) # true one error, change 5 to 6
print(check([2,4,6,4,5,6,7,8])) # true, change 6 to 4
print(check([2,4,6,8,4,5,6,7])) # false
print(check([3,8,2,5])) # false
