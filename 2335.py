class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 贪心
        # 规律
        amount.sort()
        if amount[2] > amount[1] + amount[0]:
            return amount[2]
        return (sum(amount) + 1) // 2