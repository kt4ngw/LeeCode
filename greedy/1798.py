class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        result = 0
        for i in range(len(coins)):
            if coins[i] > result + 1: # 如果当前遍历的数已经超过了前面连续的数 + 1的范围 那么就断了连续
                break
            else:
                result += coins[i]
        return result + 1
