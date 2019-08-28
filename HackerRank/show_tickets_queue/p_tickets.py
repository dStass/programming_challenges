'''
There are n people standing in line to buy show tickets.
The venue sells tickets according to the following rules:
  a.The person at the head of the line can buy exactly one ticket and must then exit the line
  
  b.if a person needs to purchase additional tickets, they must re-enter the end of the line
  and wait to be sold their next ticket(assume exit and re-entry takes zero seconds).
  
  c.Each ticket sale takes exactly one second.
  We express initial line of n people as an array, tickets = [tickets0, tickets1 … ticketsN-1],
  where ticketsi denotes the number of tickets person I wishes to buy.
  If Jesse is standing at a position p in this line, find out how much time it would take for him to buy all tickets.
'''

import sys
import time


# list of tickets [t0, t1, ..., tp, ... tN-1]
# if i < p, add p if tix[i] > tix[p] else add tix[i]
# if i > p and tix[i] < tix[p], we add tix[i] else add tix[p]-1
# add tix[p]
#
# People in FRONT of p will either:
#   1) Get all their tickets IF ticket count less than OR equal p's tikets
#   2) if they have more tickets than p's, they will only get the same amount of
#      tickets p gets before timer stops
#
# People behind p similarly will:
#   1) get all their tickets if they want less tickets than p
#   2) get the same amount of tickets as p MINUS 1 (as they are behind)
#      and timer stops before they get their pth ticket
#
# Finally we add the amount of tickets p wants
# Here tickets amounts to the same amount of time
#
def p_time(p, tickets):
  t1 = time.time()
  total_seconds = 0
  for i in range(0, len(tickets)):
    if i < p:
      total_seconds += tickets[p] if tickets[i] > tickets[p] else tickets[i]
    elif i == p:
      total_seconds += tickets[p]
    else:
      total_seconds += tickets[p]-1 if tickets[i] > tickets[p] else tickets[i]
  print("p_time time taken = ", (time.time() - t1))
  return total_seconds




# interesting result:
# assume p < N
# Logic: for list of N items from [0 . . . N-1]
# When we pop the queue at any position k, add k-1 to the end of the list
# Assume when we pop 1, 0 is added to the end of the list and negative numbers
# are never added
# time for every pop is 1 second
# So, our list contains: [0, 1, 2, ..., p, ..., N-1]
# We can approach this problem by considering two lists (conjoined)
# One list [0, 1, 2, ..., p] (let's call L1) joined to [p+1, p+2, ..., N-1] (L2)
#
# Consider L1:
# it will first take p seconds for p will be at the start of the list
# after p seconds, queue = [p, 1, 2, ..., p-2]
# or after p+1 seconds, queue = [1, 2, ..., p-1]
# now it will take ((p+1)-1) seconds for p term of interest to be at the end of list
# Therefore, we have (p+1) + (p) + p-1 + ...
# sum total = ((p+1)(p+2))/2
#
# Consider L2:
# We have [p+1, p+2, ..., N-1]
# There are N-1-p (or N-p-1 elements in this list)
# L1 is "looped" (defined when pth variable is at the end of L1) p times
# As such for p'th object will traverse an extra p * (N-p-1) seconds
# Total = sum of t(L1) and t(L2) = ((p+1)(p+2))/2 + p(N-p-1) seconds
def p_time_natural_sorted(p, N):
  t1 = time.time()
  if p < 0 or p >= N:
    return 0
  solution = 0.5*((p+2)*(p+1)) + (p)*(N-p-1)
  # or solution = 0.5*((p)*(p+1)) + (p)*(N-p) + 1
  print("p_time_natural_sorted time taken = ", time.time() - t1)
  return int(solution)


p = 1455
N = 20000026
tickets = [11,2,5,9,4]

tickets_natural = list(range(1, N+1))


# print("time for p = ", p, ", tix = ", tickets, ", t = ", p_time(p, tickets), sep='')
print("time for p = ", p, ", tix = ", len(tickets_natural), ", t = ", p_time(p, tickets_natural), sep='')
print("time for p = ", p, ", tix = ", N, ", t = ", p_time_natural_sorted(p, N), sep='')