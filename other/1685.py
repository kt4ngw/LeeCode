class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        numsSum = sum(nums)
        if numsSum < x:
            return -1

        right = 0 # 右指针
        leftSum = 0 # 左边窗口和
        rightSum = sum(nums) # 右边窗口和
        result = len(nums) + 1
        for left in range(-1, len(nums) - 1): # 左指针
            if left != -1:
                leftSum += nums[left]
            while(right < len(nums) and leftSum + rightSum > x):
                rightSum -= nums[right]
                right += 1
            if(leftSum + rightSum == x):
                result = min(result, left + 1 + len(nums) - right)
        if (result > len(nums)):
            return -1
        else:
            return result

