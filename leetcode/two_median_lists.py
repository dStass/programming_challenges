import math

class Solution:
  
  def findMedianSortedArrays(self, nums1, nums2):
    total_length = len(nums1) + len(nums2)
    required = math.floor((total_length + 1) / 2)
    if total_length % 2 == 0:
      required += 1
    
    merged = []
    
    old_i1, old_i2 = 0, 0
    i1, i2 = 0, 0
    
    while len(merged) < required:
      print("nums1:", nums1[i1:], "nums2:", nums2[i2:], "merged:", merged)

      if len(nums1) - i1 == 0 or len(nums2) - i2 == 0:
        nums, i = nums1, i1 
        if len(nums2) - i2 != 0:
          nums, i = nums2, i2
        merged += nums[i:i+required + 1]
        continue
        
      if len(nums1) - i1 == 1 and len(nums2) - i2 == 1:
        if nums1[i1] <= nums2[i2]:
          merged.append(nums1[i1])
          i1 += 1
        else:
          merged.append(nums2[i2])
          i2 += 1
        continue

      if len(nums1) - i1 == 1 or len(nums2) - i2 == 1:
        if len(nums1) - i1 == 1 and nums1[i1] <= nums2[i2]:
          merged.append(nums1[i1])
          i1 += 1
          continue
        if len(nums2) - i2 == 1 and nums2[i2] <= nums1[i1]:
          merged.append(nums2[i2])
          i2 += 1
          continue
        
      # if len(nums1) - i1 == 1 or len(nums2) - i2 == 1:
      #   if len(nums1) - i1 == 1:
      #     if nums1[i1] <= nums2[i2]:
      #       merged.append(nums1[i1])
      #       i1 += 1
      #     else:
            
      #   else:
      #     if nums2[i2] <= nums1[i1]:
      #       merged.append(nums2[i2])
      #       i2 += 1
      #     else:

      if len(nums1) - i1 != 1 and (nums1[i1] <= nums2[i2] or len(nums2) - i2 == 1):
        while True:
          jump = math.floor((len(nums1) - i1)/2)
          i1 += jump
          # print("newi1 = ", i1,i2, "oldi=", old_i1)
          if i1 >= nums2[i2] or jump == 0:
              break
          # i1 = new_i1
        merged += nums1[old_i1:i1]
        old_i1 = i1
      else:
        print('yek')
        while True:
          jump = math.floor((len(nums2) - i2)/2)
          i2 += jump
          print("newi2 = ", i2, "oldi=", old_i2, i2, nums1[i1])

          if i2 >= nums1[i1] or jump == 0:
              break
          # i2 = new_i2
        merged += nums2[old_i2:i2]
        old_i2 = i2
    
    print("required=", required, merged)
    if total_length % 2 == 1:
      return merged[required-1]
    else:
      return (merged[required-1] + merged[required-2]) / 2

          
l1 = [2]
l2 = [1, 3, 4, 5]
print(Solution().findMedianSortedArrays(l1,l2))