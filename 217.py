class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
                return True
        return False