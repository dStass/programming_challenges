class Solution:
  def maxSubArrayLen(self, nums, k):
    previous_sums = {0:-1}
    longest = 0
    running_sum = 0
    for i in range(len(nums)):
      running_sum += nums[i]
      if running_sum not in previous_sums:  # avoid re-writing where this sum as been seen before (otherwise we are writing a higher index i)
        previous_sums[running_sum] = i
      difference = running_sum - k
      if difference in previous_sums:
        longest = max(longest, i - previous_sums[difference])
        
    return longest
      
s = Solution()

nums = [1, 2, -3, 3, -1, 2, 4]
k = 3
print(s.maxSubArrayLen(nums, k))