'''
Problem: H-Index
From: Daily Interview Pro 29/10/2019

The h-index is a metric that attempts to measure the productivity
and citation impact of the publication of a scholar.
The definition of the h-index is if a scholar has
at least h of their papers cited h times. 

Given a list of publications of the number of citations a scholar has,
find their h-index.

Example:
Input: [3, 5, 0, 1, 3]
Output: 3
Explanation:
There are 3 publications with 3 or more citations, hence the h-index is 3.
'''

def hIndex(publications):
  if len(publications) == 0:
    return 0
  publications.sort(reverse=True)
  max_pubs = publications[0]
  last = -1
  h_index = 0
  for i in range(1, min([len(publications), max_pubs+1]) + 1):
    if last > 0:
      if last >= i and publications[i-1] >= i:
        h_index += 1
      else:
        break
    else:
      if publications[i-1] >= i-1:
        print(publications[i-1])
        h_index = 1
      else:
        break
      last = publications[i-1]
  return h_index

# print(hIndex([5, 3, 3, 1, 0]))
# 3

print(hIndex([0]))
# print(hIndex([100]))
# print(hIndex([1,7,3,2,3]))
