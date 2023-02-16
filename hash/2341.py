class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        dic = dict()
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        for i in dic:
            result[0] += dic[i] // 2
            result[1] += dic[i] % 2

        return result

