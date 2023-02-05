class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 1 第一想法就是遍历
        numLen = len(nums)

        """ 
        posNumCount = 0
        negNumCount = 0
        for i in range(numLen):
            if nums[i] < 0:
                negNumCount += 1
            elif nums[i] > 0:
                posNumCount += 1
        return max(negNumCount, posNumCount) """
        # 2 二分
