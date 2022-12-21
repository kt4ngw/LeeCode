class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        list = [a, b, c]
        list.sort()
        if(list[0] + list[1] <= list[2]):
            return list[0] + list[1]
        return list[2] + (list[0] + list[1] - list[2]) // 2
