class Solution:
    def minimumTotal(self, triangle) -> int:
        result = triangle
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    result[i][j] = result[i][j] + result[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    result[i][j] = result[i][j] + result[i - 1][j - 1]
                else:
                    if result[i][j] + result[i - 1][j - 1] < result[i][j] + result[i - 1][j]:
                        result[i][j] = result[i][j] + result[i - 1][j - 1]
                    else:
                        result[i][j] = result[i][j] + result[i - 1][j]
        return min(result[-1])