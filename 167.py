class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 常量级的辅助空间
        # 1 直接双for暴力  暴力破解失败
        # 2 二分查找 target - numbers[i] # 也失败 最后一个通过不了
        # 因为第一次写二分多创了许多无用变量
        # 3 二分可通过
        numLen = len(numbers)
        for i in range(numLen):
            left = i + 1
            right = numLen - 1
            while(left <= right):
                mid = int((left + right) / 2)
                if(target - numbers[i] < numbers[mid]):
                    right = mid - 1
                elif(target - numbers[i] > numbers[mid]):
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]






