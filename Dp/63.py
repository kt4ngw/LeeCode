class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        result = obstacleGrid
        if obstacleGrid[0][0] == 1:
            result[0][0] = 0
        else:
            result[0][0] = 1
        # 将第一列和第一行先填满 result 为结果矩阵
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 0:
                result[0][col] += result[0][col - 1]
            else:
                result[0][col] = 0
        for row in range(1, len(obstacleGrid)):
            if obstacleGrid[row][0] == 0:
                result[row][0] += result[row - 1][0]
            else:
                result[row][0] = 0
        # - - - - - - - - - - - - - - - - - - - - - - - - #
        # 从第二行第二列开始
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    result[i][j] += result[i - 1][j] + result[i][j - 1]
                else:
                    result[i][j] = 0
        return result[-1][-1]
