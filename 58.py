class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        length = 0
        for i in range(len(l) - 1, -1, -1):
            if len(l[i]) != 0:
                length = len(l[i])
                break
        return length