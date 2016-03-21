class Solution(object):
    def __init__(self):
        self.rowMax = 0
        self.colMax = 0
        self.lengthMatrix = []

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix == []:
            return 0

        self.rowMax = len(matrix)
        self.colMax = len(matrix[0])

        if self.rowMax == 1 and self.colMax == 1:
            return 1

        # store current longest path length
        longest = 0

        # initialize max increasing path length for each node
        self.lengthMatrix = [x[:] for x in [[0] * self.colMax] * self.rowMax]

        for i in range(self.rowMax):
            for j in range(self.colMax):
                longest = max(self.dfs(i, j, matrix), longest)

        return longest

    def dfs(self, row, col, matrix):
        if self.lengthMatrix[row][col] == 0:
            # 1. this node hasn't been visited, do dfs for its four directions
            # 2. only do dfs if neighbor nodes' value larger than this node's value
            self.lengthMatrix[row][col] = max(
                self.dfs(row + 1, col, matrix) if row + 1 < self.rowMax and matrix[row + 1][col] > matrix[row][col] else 0,
                self.dfs(row - 1, col, matrix) if row - 1 > -1 and matrix[row - 1][col] > matrix[row][col] else 0,
                self.dfs(row, col + 1, matrix) if col + 1 < self.colMax and matrix[row][col + 1] > matrix[row][col] else 0,
                self.dfs(row, col - 1, matrix) if col - 1 > -1 and matrix[row][col - 1] > matrix[row][col] else 0
            ) + 1

        return self.lengthMatrix[row][col]






test = Solution()
nums1 = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(test.longestIncreasingPath(nums1))

nums2 = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

print(test.longestIncreasingPath(nums2))

nums3 = []
print(test.longestIncreasingPath(nums3))
