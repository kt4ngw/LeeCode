class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for 循环 暴力
        # 第二种KMP 之后写
        for i in range(len(haystack) - len(needle) + 1):
            pointLeft = i
            pointRight = 0
            while(pointRight < len(needle)):
                if haystack[i] == needle[pointRight]:
                    i += 1
                    pointRight += 1
                else:
                    break
            if pointRight == len(needle):
                return pointLeft

        return -1