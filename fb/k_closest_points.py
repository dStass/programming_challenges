import heapq
import math

class Solution:
  def __init__(self):
    pass
  
  def k_closest(self, k, points):
    if k > len(points):  # o(1)
      return points

    k_points = []
    heapq.heapify(k_points)  # o(1)

    for point in points: # o(n)
      dist = self.dist_from_origin(point)
      tup = (-dist, point)
      self.insert(k_points, k, tup)
    
    # return k_points
    return [point[1] for point in k_points]
    
  def dist_from_origin(self, point):
    return math.sqrt(point[0]**2 + point[1]**2)
  
  def insert(self, k_points, k, tup):  #(log(k))
    heapq.heappush(k_points, tup)
    if len(k_points) > k:
      heapq.heappop(k_points)



sol = Solution()

K = 3
points = [[-1,0],[0,1], [1,1],[0,0],[1,0],[-1,-1]]

k_closest = sol.k_closest(K, points)
print(k_closest)