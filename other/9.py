class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # 取余 除10能除断
            return False
        elif x == 0:
            return True
        else: # 大于0
            list = []
            while(x != 0):
                list.append(x % 10)
                x = x // 10
        # x % 10  最后一个数
        # x // 10 删除该数最后一位数剩下的数
            for i in range(int(len(list) / 2)):
                if(list[i] != list[len(list) - i - 1]):
                    return False    
            return True



