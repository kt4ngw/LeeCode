class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float('inf')] * n for _ in range(n)] for _ in range(2)]
        dp[0][0][0] = 0  # 初始蛇尾巴位置的步数
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue  # 有障碍此路不通

                # 1. 当前是水平状态
                if j + 1 < n and grid[i][j + 1] == 0:
                    if i - 1 >= 0:  # 1.1 从上一行移下来的
                        dp[0][i][j] = min(dp[0][i][j], dp[0][i - 1][j] + 1)
                    if j - 1 >= 0:  # 1.2 从左边移过来的的
                        dp[0][i][j] = min(dp[0][i][j], dp[0][i][j - 1] + 1)
                    if i + 1 < n and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                        # 1.3 从水平转到垂直
                        dp[1][i][j] = min(dp[1][i][j], dp[0][i][j] + 1)

                        # 2. 当前是垂直状态
                if i + 1 < n and grid[i + 1][j] == 0:
                    if j - 1 >= 0:  # 2.1 从前一列平移到下一列的
                        dp[1][i][j] = min(dp[1][i][j], dp[1][i][j - 1] + 1)
                    if i - 1 >= 0:  # 2.2 从上面移下来的一格的
                        dp[1][i][j] = min(dp[1][i][j], dp[1][i - 1][j] + 1)
                    if j + 1 < n and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                        # 2.3 从垂直转到水平
                        dp[0][i][j] = min(dp[0][i][j], dp[1][i][j] + 1)

        return dp[0][n - 1][n - 2] if dp[0][n - 1][n - 2] != float("inf") else -1
