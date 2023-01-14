class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 特殊情况
        # 凑不了怎么办 数组最后面一个还是原来的值，就是不满足条件
        dp = [amount + 1] * (amount + 1)  #
        dp[0] = 0
        for i in range(0, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if (dp[-1] != amount + 1):
            return dp[-1]
        else:
            return -1




