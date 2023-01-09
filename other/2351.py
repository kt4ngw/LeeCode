class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # 一个 a - z 的数组 两列
        # 第一列 记录 出现次数 第二列记录出现第二次出现的位置 如果在第二列出现了，就可以确定是这个，直接break，那么第三次出现怎么办？第三次直接 已经break了

        arr = [[0] * 2 for i in range(26)]
        for i in range(len(s)):
            if arr[ord(s[i]) - 97][0] == 0:
                arr[ord(s[i]) - 97][0] = 1  # 出现了第一个
            else:  # 第一个已经出现
                arr[ord(s[i]) - 97][1] = i + 1
                break
        for i in range(26):
            if(arr[i][0] == 1 and arr[i][1]>0):
                return chr(i + 97)