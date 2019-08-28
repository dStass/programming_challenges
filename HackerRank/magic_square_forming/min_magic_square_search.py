#!/bin/python3

import math
import os
import random
import re
import sys

MAX_NUMBER = 10
COST_INDEX = 9
MAGIC_SUM = 45

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # 3x3 magic squares, some const:


    sq = []
    for i in s:
        sq.extend(i)
    sq.append(0)  # into a list with weight in index 9

    queue = []
    visited = {}
    queue.append(sq)
    visited[str(sq[:-1])] = 0

    while queue:
        curr = queue.pop(0)

        square = curr[:-1]
        
        if isMagic(square):
            print(curr)
            return curr[COST_INDEX]

        # generate next nodes
        for i in range(MAX_NUMBER - 1):
            if i == 4 and curr[i] != 5:
                continue
                
            # print("yeet qsize=", len(queue))
            childp = curr.copy()
            if childp[i] < MAX_NUMBER - 1:
                childp[i] += 1
                childp[COST_INDEX] += 1
                if visited.get(str(childp[:-1])) == None:
                    # if abs(MAGIC_SUM - sum(childp[:-1])) <= abs(MAGIC_SUM - sum(curr[:-1])):
                        # print("yeehaw", sum(childp[:-1]))
                    insertSorted(queue, childp)
                    visited[str(childp[:-1])] = childp[COST_INDEX]

            childm = curr.copy()
            if childm[i] > 1:
                childm[i] = childm[i] - 1
                childm[COST_INDEX] += 1
                if visited.get(str(childm[:-1])) == None:
                    # if abs(MAGIC_SUM - sum(childm[:-1])) <= abs(MAGIC_SUM - sum(curr[:-1])):
                        # print(childm[:-1])
                        # print("diff", abs(MAX_NUMBER - sum(childm[:-1])), "itself ", sum(childm[:-1]))
                    
                    insertSorted(queue, childm)
                    visited[str(childm[:-1])] = childm[COST_INDEX]
             
    return 0

def isMagic(s):
    for i in range(3):
        # row: i = 0, check 0,1,2
        # i = 1 check 3,4,5
        # i = 2, check 6,7,8
        # row = 3*i + [0,1,2]
        r1 = 3*i + 0
        r2 = 3*i + 1
        r3 = 3*i + 2
        rowsum = s[r1] + s[r2] + s[r3]
        if rowsum != 15:
            return False

        # col: i = 0, check 0, 3, 6
        # i = 1, check 1, 4, 7
        # i = 2, check 2, 5, 8
        # i + [0,3,6]
        c1 = i + 0
        c2 = i + 3
        c3 = i + 6
        colsum = s[c1] + s[c2] + s[c3]
        if colsum != 15:
            return False
    return True

def insertSorted(q, s):
    heus = abs(MAGIC_SUM - sum(s[:-1]))
    for i in range(len(q)):
        heui = abs(MAGIC_SUM - sum((q[i])[:-1]))
        if (s[COST_INDEX] + heus) < (q[i][COST_INDEX] + heui + 1):
            q.insert(i, s)
            return
    q.append(s)
    return


s = []
s.append([4,8,2])
s.append([4,5,7])
s.append([6,1,6])

result = formingMagicSquare(s)
print("result=", result)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = []

#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))

#     result = formingMagicSquare(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
