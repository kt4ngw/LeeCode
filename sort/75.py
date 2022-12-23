class Solution:
    def sortColors(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, List, low, high):
        if (low < high):
            p = self.Partition(List, low, high)  # 划分左右数组
            self.quick_sort(List, low, p - 1)  # 依次对左右数组递归
            self.quick_sort(List, p + 1, high)
            return List
        """
        Do not return anything, modify nums in-place instead.
        """
        # 常见的排序算法都能解决这道问题

    def Partition(self, List, low, high):  # 一趟划分
        pivot = List[low]  # 以数组第一个元素为基准 划分数组
        while (low < high):  # 循环控制
            while (low < high and List[high] >= pivot):
                high = high - 1
            List[low] = List[high]  # 比基准元素小的去基准元素左边
            while (low < high and List[low] <= pivot):
                low = low + 1
            List[high] = List[low]  # 比基准元素大的去基准元素右边
        List[low] = pivot
        return low  # 返回基准元素的位置，用来递归划分





