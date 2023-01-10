class Solution:
    # 暴力解法
    # 第一个for循环先把perm打乱
    # 然后暴力的利用 for循环对打乱的perm数组进行恢复 看需要多少步才能回到初始的数组 step来记录需要多少步
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        arr = perm.copy()
        for i in range(n):
            if (i % 2 == 0):
                arr[i] = perm[int(i / 2)]
            else:
                arr[i] = perm[int(n / 2 + (i - 1) / 2)]
        perm = arr.copy()
        step = 1  # 记录需要多少步 打乱已经用了一步
        while (True):
            if (perm == [i for i in range(n)]): # 如果和初始数组一样，那么就退出恢复数组的for循环
                break
            for i in range(n):
                if (i % 2 == 0):
                    arr[i] = perm[int(i / 2)]
                else:
                    arr[i] = perm[int(n / 2 + (i - 1) / 2)]
            perm = arr.copy()
            step += 1
        return step



# 模拟推理

class Solution:
    # 非暴力解法

    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        arr = perm.copy()

        return step



# 数论