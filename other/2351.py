class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0  # 计数 *
        count_ = 0  # 计数 “|”
        for i in s:
            if i == '|':
                count_ += 1
            elif (count_ % 2 == 0 and i == '*'):
                count += 1
        return count
        # 什么情况下去计数 count ? 做一个flag标记