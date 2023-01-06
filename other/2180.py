class Solution:
    def countEven(self, num: int) -> int:

        # 暴力破解
        count = 0
        for i in range(1, num + 1):
            strTemp = str(i)
            res = 0
            for i in strTemp:
                res += int(i)
            if res % 2 == 0:
                count += 1
        return count