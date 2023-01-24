class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while (True):
                if nums[i] >= 1 and nums[i] <= len(nums) and nums[i] != i + 1:
                    # 1 1 2 就卡死在这里无限循环
                    if nums[nums[i] - 1] == nums[i]:
                        break
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return i + 2

