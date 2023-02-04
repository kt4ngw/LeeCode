class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 二分， 在1 ~ num/2中找num的开方数字，如果找到那就是存在，没找到就是没有 
        left = 1
        right = num // 2 if num != 1 else 1
        while(left <= right):
            sqrt = (left + right) // 2
            if(sqrt * sqrt > num):
                right = sqrt - 1
            elif (sqrt * sqrt < num):
                left = sqrt + 1
            else:
                return True
        return False