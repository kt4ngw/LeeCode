class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 枚举不可行
        slideWindow = ''
        length = len(slideWindow)
        for i in s:
        # check 这个窗口是否合适 i字符是否存在于slideWindow中 如果不存在那么就加入到slideWindow中
        # 如果存在 那么就滑动 寻找新的slideWindow
        # if i not in slideWindow then slideWindow+=i
        # else i in S
            flag = 0 # 不存在的意思
            for k in range(len(slideWindow)):
                if i == slideWindow[k]: # 如果发现slideWindow中有这个字符，那么就要从这个字符开始截断，从下一个字符开始新的滑动窗口
                    slideWindow = slideWindow[k + 1:] + i
                    flag = 1
                    break
            if flag == 0:
                slideWindow += i
            length = max(length, len(slideWindow))
        return length