class Solution:
    def minPathSum(self, grid) -> int:
        dp = [[0] * len(grid[0])] + [[0] + [0] * (len(grid[0]) - 1) for _ in range(len(grid) - 1)]
        for k in range(len(grid[0])):
            if(k == 0):
                dp[0][k] = grid[0][k]
            else:
                dp[0][k] = dp[0][k - 1] + grid[0][k]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            for j in range(1, len(grid[0])):
                if dp[i][j - 1] + grid[i][j] > dp[i - 1][j] + grid[i][j]:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
        return dp[len(grid) - 1][len(grid[0]) - 1]


