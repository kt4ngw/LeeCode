class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1 排序 然后遍历 时间复杂度最好O（logn）
        # 2 置换，遍历一遍，对小于等于数组长度的值放到跟其值相同的数组数组下标处，
        #  最后再遍历一次查找数组下标和值是否对应。如果不对应就输出下标，如果全部对应，就输出数组最后一个值加1
        numLen = len(nums) # 9
        for i in range(numLen):
            while(True):
                if nums[i] < numLen and nums[i] != i:
                    nums[nums[i]], nums[i] =  nums[i], nums[nums[i]]
                else:
                    break
        for i in range(numLen):
           if i != nums[i]:
               return i
        return nums[-1] + 1
