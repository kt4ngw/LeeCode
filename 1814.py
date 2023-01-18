class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # n n - 1 n - 2 n - 3 n - 4
        # O(n^2)
        # 暴力破解会失败 尝试过一次
        # 思路是 遍历nums 求nums[下标] - rev(nums[下标])的值及其对应的个数，最后求组合数（排列组合）
        def rev(number):  # 反转该数
            revNumber = 0
            while (number):
                revNumber = revNumber * 10 + number % 10
                number = number // 10
            return revNumber

        dict = {}  # 用来存放 nums[i] - rev(nums[i])的值及其对应的个数
        for i in range(len(nums)):
            if nums[i] - rev(nums[i]) not in dict:
                dict[nums[i] - rev(nums[i])] = 1  #
            else:
                dict[nums[i] - rev(nums[i])] += 1
        count = 0
        import math
        for i in dict.values():
            if i >= 2:  # nums[i] - rev(nums[i])的值大于两次才算一对
                count += math.comb(i, 2)  # 求组合数 C 多少取 2 就是有多少对
        return count % (10 ** 9 + 7)