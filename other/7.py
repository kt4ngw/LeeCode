class Solution:
    def reverse(self, x: int) -> int:
        # 将数字转化成字符串来 反转
        s = str(x)
        newS = ''
        for i in range(len(s) - 1, -1 , -1):
            if(s[i] == '-'):
                newS = s[i] + newS
            else:
                newS += s[i]

        if int(newS) > 2 ** 31 - 1 or int(newS) < - 2 ** 31: # 条件判断
            return 0
        else:
            return int(newS)
