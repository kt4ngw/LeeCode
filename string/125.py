class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringPalindrome = ''
        for i in s:
            if i <= 'z' and i >= 'a':
                stringPalindrome += i
            elif i <= 'Z' and i >= 'A':
                stringPalindrome += i.lower()
            elif i <= '9' and i >= '0':
                stringPalindrome += i
            else:
                continue
        if stringPalindrome == '':
            return True
        left = 0
        right = len(stringPalindrome) - 1
        flag = 1 # 标记是不是回文串
        while(left <= right): # right > 0 是判断不是空字符串
            if stringPalindrome[left] != stringPalindrome[right]:
                flag = 0
                break
            left += 1
            right -= 1
        return True if flag == 1 else False