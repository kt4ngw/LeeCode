class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 限定了时间复杂度 那么就是二分
        left = 0
        right = len(nums) - 1
        if left == right:
            return left
        while(left <= right):
            mid = (left + right) // 2
            # 0 和 len(nums) - 1特殊情况
            if mid == 0:
                if nums[mid + 1] < nums[mid]:
                    return mid
                else:
                    left = mid + 1
                continue
            if mid == right:
                if nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    right = mid - 1
                continue
            # 0 和 len(nums) - 1特殊情况
            if(nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]):
                # 1 2 1
                return mid
            elif(nums[mid - 1] < nums[mid] and nums[mid + 1] > nums[mid]):
                # 1 2 3
                left = mid + 1
            elif(nums[mid - 1] > nums[mid] and nums[mid + 1] < nums[mid]):
                # 3 2 1
                right = mid - 1
            else:
                # 2 1 2
                r = random.randint(0, 1)
                if r == 1:
                    left = mid + 1
                else:
                    right = mid - 1