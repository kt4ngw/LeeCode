class Solution:
    def minimumTotal(self, triangle) -> int:
        output = 0
        for i in range(len(triangle)):
            output = output + min(triangle[i])
        return output


c = Solution()
print(c.minimumTotal([[-1],[2,3],[1,-1,-3]]))
print(-1 + 2 - 3)