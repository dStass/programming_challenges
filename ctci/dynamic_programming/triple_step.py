'''
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs. 
'''


def num_ways(n):
  # planning:
  # 1 step: 1 way (take 1 step)
  # 2 steps: 2 ways (take 1 double step or 2 single steps)
  # 3 steps: (1+1+1, 1+2, 2+1, 3) 4 ways

  tally = []
  tally.append(1)
  tally.append(2)
  tally.append(4)

  if n < 3:
    return tally[n]

  for i in range(3, n+1):
    # calculate the last step the child makes
    ith_total_steps = tally[i-1] + tally[i-2] + tally[i-3]
    tally.append(ith_total_steps)
  
  return tally[-1]


print(num_ways(100))