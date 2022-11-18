class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = size * [0]
        dp[0] = nums[0]
        if size > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[size - 1]
