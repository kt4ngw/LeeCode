class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 2 3 1 1 4
        if len(nums) == 1: # 特殊情况
            return True
        maxJump = 1 # 可跳的最远位置 初始位置为1 ，如果max > len(nums) true 否则 false
        for i in range(1, len(nums)):
            if maxJump < i: # 最远的位置还跳不到遍历下标 直接返回false
                return False
            tempJump = i + nums[i - 1]
            maxJump = max(maxJump, tempJump)
            if maxJump >= len(nums):
                return True
        return False