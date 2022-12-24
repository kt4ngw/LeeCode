class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 每一次删除这一行的最大值，然后比较各行最大的元素
        res = 0
        for i in range(len(grid)):
            grid[i].sort()
        for j in range(len(grid[0])):
            max = grid[0][j]
            for i in range(len(grid)):
                if grid[i][j] > max:
                    max = grid[i][j]
            res += max
        return res
