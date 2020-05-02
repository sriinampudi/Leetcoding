# Problem 1351
#Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#Return the number of negative numbers in grid.

#Example:

#Input: grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.
def countNegatives(grid):
        negative_count = 0
        for row in grid:
                for element in row:
                        if element < 0:
                                 negative_count += 1
        return negative_count


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print("Number of negative numbers in the matrix: {}".format(countNegatives(grid)))
