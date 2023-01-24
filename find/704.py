class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySerch(arr, target):
            # 二分查找
            left = 0
            right = len(arr) - 1
            mid = 0
            while (left <= right):
                mid = int((left + right) / 2)
                if (target < arr[mid]):
                    right -= 1
                elif (target > arr[mid]):
                    left += 1
                else:
                    return mid
            return -1

        return binarySerch(nums, target)