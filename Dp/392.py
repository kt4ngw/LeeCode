class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s是否是t的子序列 abc ahbgdc
        flag = 0 # flag == 1 是子序列
        if(s != ""):
            a = 0
            for i in range(len(t)):
                if(t[i] == s[a]):
                    a = a + 1
                if(a == len(s)):
                    flag = 1
                    break
        else:
            flag = 1
        if(flag == 1):
            return True
        else:
            return False


c = Solution()
print(c.isSubsequence("b", "c"))