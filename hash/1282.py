class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # hash 存储
        dic = dict()
        result = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dic:
                dic[groupSizes[i]] = [i]
            else:
                dic[groupSizes[i]].append(i)
            if len(dic[groupSizes[i]]) == groupSizes[i]:
                result.append(dic[groupSizes[i]])
                dic[groupSizes[i]] = []
        return result
