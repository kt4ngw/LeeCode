class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        f = nums[0] # 记录遍历的时候连续序列的值 哪个大 记录哪个

        for i in range(1, len(nums)):
            f = f + nums[i]
            maxSum = max(f, maxSum, nums[i])
            if f < nums[i]: # 如果前面连续序列的值的和 还小于当前遍历的这个值，那么就从该值开始记录连续序列
                f = nums[i]
        return maxSum