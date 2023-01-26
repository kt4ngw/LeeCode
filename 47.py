class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(nums, temp):
            if 0 == len(nums):
                result.append(temp)
            else:
                for i in range(len(nums)):
                    # 从 i 之前能找到
                    flag = 1  # 首先没有相同的
                    piont = i
                    while (piont >= 1):
                        if (nums[i] == nums[piont - 1]):
                            flag = 0
                            break
                        piont -= 1
                    if flag == 1:
                        backtrack(nums[:i] + nums[i + 1:], temp + [nums[i]])

        backtrack(nums, [])
        return result