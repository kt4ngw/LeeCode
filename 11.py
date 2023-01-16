class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1 # j = 8
        # 双指针 一个指向开头，一个指向末尾
        area = 0
        while(i != j):
            area = max((j - i) * min(height[i], height[j]), area)
            if(height[i] > height[j]):
                j -= 1
            else:
                i += 1
        return area