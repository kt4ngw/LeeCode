class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 从后往前遍历，假设在当前指针前的数值都为1，
        # k就是当前遍历点和之前的数值之和，
        # 用一个temp临时变量存放当前值应该填什么字母（应该填充的数就是 k - 在当前指针前面数的和（此处为i）），
        # 判断的时候如果小于26 就这个数，如果大于26，就填26，
        # 思想就是大数全放后面存，小数到前面去
        result = ''  # 存放答案
        for i in range(n - 1, -1, -1):
            temp = k - (i) * 1  #
            result = chr(min(temp, 26) + 96) + result
            k = k - min(temp, 26)
        return result


