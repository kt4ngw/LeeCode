class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 规定了时间复杂度 那么只能用二分查找
        def binarySearchFindLeft(arr, target):
            left = 0
            right = len(arr) - 1
            mid = 0
            while (left <= right):
                mid = int((left + right) / 2)
                if (target < arr[mid]):
                    right = mid - 1
                elif (target > arr[mid]):
                    left = left + 1
                else:
                    while (True):
                        if (mid - 1 >= 0 and arr[mid - 1] == target):
                            mid = mid - 1
                        else:
                            return mid
            return -1  # 不存在

        def binarySearchFindRight(arr, target):

            left = 0
            right = len(arr) - 1
            mid = 0
            while (left <= right):
                mid = int((left + right) / 2)
                if (target < arr[mid]):
                    right = mid - 1
                elif (target > arr[mid]):
                    left = left + 1
                else:
                    while (True):
                        if (mid + 1 <= len(arr) - 1 and arr[mid + 1] == target):
                            mid = mid + 1
                        else:
                            return mid
            return -1  # 不存在

        res = []
        res.append(binarySearchFindLeft(nums, target), )
        res.append(binarySearchFindRight(nums, target), )

        return res