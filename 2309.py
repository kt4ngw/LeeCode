class Solution:
    def greatestLetter(self, s: str) -> str:
        arr = [[False] * 2 for i in range(26)] # 左边存储是否有小写，右边是否有大写
        # ASCII码和数组下标的转换
        for i in s: 
            # i是一个字符
            if 65 <= ord(i) and ord(i) <= 90: # 大写
                arr[ord(i) - 65][1] = True
            else:
                # 97 ~ 122
                arr[ord(i) - 97][0] = True
        res = 0 
        for i in range(len(arr)):
            if arr[i][0] == True and arr[i][1] == True:
                res = i + 65
        return chr(res) if res != 0 else "" # 如果 res有变动那么就有“最好英文字母”出现 否则返回空
        # 时间复杂度 O（N + 26） N为字符串长度 26为字母总长