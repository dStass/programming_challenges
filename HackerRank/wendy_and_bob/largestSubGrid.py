def largestSubgrid(grid, maxSum):
    greatestBelowMaxSum = 0
    mySubGridLen = 0
    gridLength = len(grid)
    for subGridLen in range (1, gridLength + 1):
        for i in range(gridLength + 1 - subGridLen):
            for j in range(gridLength + 1 - subGridLen):
                subGridSum = getSubGridSum(grid, i, j, subGridLen)
                if subGridSum >= greatestBelowMaxSum and subGridSum <= maxSum:
                    greatestBelowMaxSum = subGridSum
                    mySubGridLen = subGridLen
    return mySubGridLen

def getSubGridSum(grid, x, y, gridLength):
    if gridLength == 1:
        return grid[x][y]
    mySum = 0
    toAdd = gridLength - 1
    for j in range(y, y+gridLength):
        for i in range(x, x+gridLength):
            mySum += grid[i][j]
    

    return mySum
print(largestSubgrid([[1,2,3],[2,5,1], [1,2,3]], 4))

# print(largestSubgrid([[1,1,1,1],[2,2,2,2], [3,3,3,3], [4,4,4,4]], 0))
