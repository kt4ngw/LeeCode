class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        maxLong = 0
        for i in range(len(s)):
            if i == 0:
                if s[i] == '(' or s[i] == ')':
                    dp[i] = 0
                    continue
            if i == 1:
                if s[i - 1] == '(' and s[i] == ')':
                    dp[i] = 0 + 2
                else:
                    dp[i] = 0
                maxLong = max(maxLong, dp[i])
                continue
            if s[i] == '(':
                dp[i] == 0
            else:
                if s[i] == ')' and s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i] == ')' and s[i - 1] == ')':
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = dp[0]
                else:
                    dp[i] = 0
            maxLong = max(maxLong, dp[i])

        return maxLong
