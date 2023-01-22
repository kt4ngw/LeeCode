class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStringLen = 0
        maxString = ""
        for i in range(len(s)):
            stringTemp = s[i]
            # 中心扩散法
            # 最多扩散多少呢？扩散到最前面的字符串
            left = i - 1
            # 向左向右寻找有没有和当前字符相等的字符
            # 左边的字符是left 右边是right
            right = i + 1
            while(left >= 0):
                if s[left] == s[i]:
                    stringTemp = s[left] + stringTemp
                else:
                    break
                left -= 1
            while(right <= len(s) - 1):
                if s[right] == s[i]:
                    stringTemp += s[right]
                else:
                    break
                right += 1
            while(True):   # 不对劲 因为 bb

                if  left >= 0 and right <= len(s) - 1 and s[left] == s[right]  :
                    stringTemp = s[left] + stringTemp + s[right]
                else:
                    break
                left -= 1
                right += 1
            if len(stringTemp) > maxStringLen:
                maxString = stringTemp
                maxStringLen = len(stringTemp)
        return maxString