class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(nums, temp):
            if 0 == len(nums):
                result.append(temp)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i] + nums[i + 1:], temp + [nums[i]])

        backtrack(nums, [])
        return result

# 回溯