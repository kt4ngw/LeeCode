class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        # case1
        dp = size * [0]
        dp[0] = nums[0]
        result = dp[0]
        if size > 1:
            dp[1] = max(nums[0], nums[1])
            result = dp[1]
        if size > 2:
            for i in range(2, size - 1):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
                # dp[-2] 是最大的

            dpNotSizeOne = size * [0]
            dpNotSizeOne[0] = nums[1]
            dpNotSizeOne[1] = max(nums[1], nums[2])
            for i in range(3, size):
                dpNotSizeOne[i - 1] = max(dpNotSizeOne[i - 1 - 1], nums[i] + dpNotSizeOne[i - 2 - 1])
            result = max(dp[-2], dpNotSizeOne[-2])

        return result
