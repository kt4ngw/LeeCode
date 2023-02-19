class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        left = 0
        right = numsLen - 1
        point = numsLen - 1
        arr = nums.copy()
        while (left <= right):
            if abs(nums[left]) > abs(nums[right]):
                arr[point] = abs(nums[left]) ** 2
                left += 1

            else:
                arr[point] = abs(nums[right]) ** 2
                right -= 1
            point -= 1
        return arr
