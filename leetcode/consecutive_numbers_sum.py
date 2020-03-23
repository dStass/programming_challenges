'''
Odd-to-Odd:
1+2+3=6 = (4*1+4/2)
1+2+3+4+5=15
1+2+3+4+5+6+7=28 (8*3+8/2)

3+4+5 = (8*1 + 8/2)
5+6+7 = (12*1 + 12/2)


2+3+4+5 -> 


1:  1 [1]
2:  1 [2]
3:  2 [1+2, 3]
4:  1 [4]
5:  2 [2+3, 5]
6:  2 [1+2+3, 6]
7:  2 [3+4, 7]
8:  1 [8]
9:  3 [2+3+4, 4+5, 9]
10: 
'''

import math

class Solution:
  def consecutiveNumbersSum(self, N: int) -> int:
    total_sum = 0
    for k in range(N, 0, -1):
      mval = self.evaluateMValue(float(k), float(N))
      if mval % 1 == 0: # is zero or positive integer
        total_sum += 1
        sum_str = '+'.join(str(x) for x in list(range(int(k),int(k) + int(mval+1))))
        print(k, mval, sum_str)
    return total_sum
 

  def consecutiveNumbersSumUsingC(self, N: int) -> int:
    total_sums = 0
    k = N
    next_c = None
    while k >= 1:
      minus_by = 1
      mval = self.evaluateMValue(float(k), float(N))  # size of Consecutive num sum (ie number of items in i_1+i_2+...+i_m)
      if mval % 1 == 0: # is zero or positive integer
        next_c = self.findNextC(k, mval, N)
        # print("gere", next_c)
        break
      k -= minus_by

        # next_c = self.findNextC(k, mval, N)
        # print("nextC = ", next_c)
        # total_sums += 1
        # sum_str = '+'.join(str(x) for x in list(range(int(k),int(k) + int(mval+1))))
        # print(k, mval, sum_str)
    
    while next_c != -1:
      k -= next_c
      mval = self.evaluateMValue(float(k), float(N))
      next_c = self.findNextC(k, mval, N)
      total_sums += 1

      # print(k, next_c)


    return total_sums + 1
  

  def findNextC(self, k, upperM, N):
    '''
    introduce c:
    substitute k for k - c
    -> 
    ie m = -(0.5 + k) + math.sqrt((0.5 + k)**2 - 2*(k - N))
    turns into:
    m = -(0.5 + k - c) + math.sqrt((0.5 + k - c)**2 - 2*(k - c - N))

    rearranging this, we have c =
    c = (2*k*m + 2*k + m^2 + m - 2*N)/(2*(m+1))
    '''

    # c = (2*k*m + 2*k + m^2 + m - 2*N)/(2*(m+1))
    # since m must be an integer, we can start subbing in for m
    # we know size of sum is bounded for every new iteration

    for m in range(int(upperM)+1, math.floor((-1 + math.sqrt(1+8*N))/2)):
      c = self.getCGivenM(k, m, N)
      # print("k = {}, m = {}, c = {}".format(k, m, c))
      if c > 0 and c%1 == 0:
        return c
    return -1

  
  def getCGivenM(self, k, m, N):
    c = (2*k + m + 2*k*m + m*m - 2*N)/(2*(1 + m))
    return c
      
  def evaluateMValue(self, k, N):
    '''
    m = -(1/2 + k) + sqrt((1/2 + k)^2 - 2(k - N))
    if m is positive integer, return -1
    else return expression
    guaranteed k < n
    '''
    m = -(0.5 + k) + math.sqrt((0.5 + k)**2 - 2*(k - N))


    return m

print("num ways = ", Solution().consecutiveNumbersSumUsingC(100000000005))