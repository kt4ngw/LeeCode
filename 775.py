class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:

        # 局部倒置 一定是全局倒置
        # 那么就找一下 除了是全局倒置的局部倒置
        count = 0
        for i in range(len(nums)):
            if max(nums[i], i) - min(nums[i], i) > 1:
                return False
        return True
