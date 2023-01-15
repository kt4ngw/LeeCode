class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # 模拟
        length = len(nums)
        while(len(nums) != 1): # 判断数组长度 如果不等于1就要循环
            newNums = [0] * int(len(nums) / 2)  # 开辟新数组存放变一半的数组
            for i in range(int(len(nums) / 2)):
                if i % 2 == 0: # 偶数下标
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    # 奇数下标
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newNums.copy() # 将新数组赋值给 原来数组的变量 为了好判断
            length = len(newNums) # 新数组的长度
        return nums[0]
