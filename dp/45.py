class Solution:
    def jump(self, nums: List[int]) -> int:
        # 从后往前推
        arr = [0] * len(nums) # 记录当前下标最小需要多少步才能跳到最后
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + (i + 1) >= len(nums): # 如果当前能跳跃到最后位置, 1步就能跳到
                arr[i] = 1 
            else:
                if nums[i] == 0:
                    arr[i] = 0
                else:
                # 1 在后面能跳到的位置里，选择步数最小的，为0的要跳过
                # 2 如果为0那么就为0
                    minStep = 100000
                    for j in range(i + 1, i + 1 + nums[i]):
                        if arr[j] == 0:
                            continue
                        else:
                            minStep = min(arr[j] + 1, minStep)
                    arr[i] = minStep
        return arr[0]