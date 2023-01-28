class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        oddSum = 0 
        evenSum = 0 
        count = 0 # 记录有多少平衡数组
        for i in range(len(nums)):
            if i % 2 != 0:
                oddSum += nums[i]
            else:
                evenSum += nums[i]
        oddSumTemp = 0 
        evenSumTemp = 0
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                if i % 2 == 0: # 偶数数
                    evenSum = evenSum - nums[i]  
                else: # 奇数
                    oddSum = oddSum - nums[i]
            else:
                if i % 2 == 0: 
                    evenSum = evenSum - nums[i]  # 2
                    evenSumTemp = evenSumTemp + nums[i + 1]  # 4
                else:
                    oddSum = oddSum - nums[i]
                    oddSumTemp = oddSumTemp + nums[i + 1]
            if(oddSumTemp + oddSum == evenSumTemp + evenSum):
                count += 1
        return count 