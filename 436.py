class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def BSearchNumber(arr, target):
            """用一个新数组存放所有的区间左值并排序，用字典存放所有区间左值对应的原数组下标，
            然后遍历原数组区间的右值，作为target，以及利用排序后的新数组去二分查找。
            最后找到的数再利用字典和原数组进行输出。
            """
            left = 0
            right = len(arr) - 1
            if(target > arr[right]):
                return -1
            while(left < right):
                mid = (left + right) // 2
                if (arr[mid] < target):
                    left = mid + 1
                elif(arr[mid] >= target):
                    right = mid

            return left

        intervalLen = len(intervals)
        result = [-1] * intervalLen
        dic = dict()
        arr = [0] * intervalLen
        for i in range(intervalLen):
            arr[i] = intervals[i][0]
            dic[intervals[i][0]] = i
        arr.sort()
        for i in range(intervalLen):
            thatNumber = BSearchNumber(arr, intervals[i][1])
            if(thatNumber == -1):
                continue
            else:
                result[i] = dic[arr[thatNumber]]

        return result

