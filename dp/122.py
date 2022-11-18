class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i in range(len(prices) - 1):
        #     if(prices[i + 1] > prices[i]):
        #         res += prices[i + 1] - prices[i]
        # return res
        # # 贪心思想

        listSize = len(prices)
        dp = [2 * [0]] * listSize
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, listSize):
            dp[i][0] = max(dp[i - 1][0], prices[i] + dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[listSize - 1][0]
