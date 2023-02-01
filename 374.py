# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while(left <= right):
            chooseNum = int((left + right) / 2)
            if guess(chooseNum) == -1:
                right = chooseNum - 1
            elif guess(chooseNum) == 1:
                left = chooseNum + 1
            else:
                return chooseNum
        # 时间复杂度O（logN） 二分查找