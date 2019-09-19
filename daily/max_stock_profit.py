'''
Problem: Maximum Profit of Stock
From: Coding Interview Pro 19/09/2019

You are given an array. Each element represents the price of a stock on that particular day.
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5,
and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
'''


# Problem: give max a[j] - a[i] such that j>i
def buy_and_sell(arr):
  if len(arr) < 2:
    return 0
  
  best = 0
  start = 0
  min_so_far = arr[0]
  for end in range(1, len(arr)):
    best = max(best, arr[end] - min_so_far)
    min_so_far = min(min_so_far, arr[end])
  return best
  
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
