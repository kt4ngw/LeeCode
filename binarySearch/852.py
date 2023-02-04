class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """ans = 0
        for i in range(len(arr)):
            if arr[i] > arr[ans]:
                ans = i
        return ans"""
        # 需要二分
        arrLen = len(arr)
        left = 0
        right = arrLen - 1
        while (left < right):
            mid = (left + right) // 2
            if (arr[mid] > arr[mid + 1]):
                right = mid

            else:  # arr[mid] < arr[mid + 1]
                left = mid + 1
        return left
