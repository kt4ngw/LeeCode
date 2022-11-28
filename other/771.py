class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        strArr = []
        count = 0
        for i in range(len(jewels)):
            strArr.append(jewels[i])
        for i in range(len(stones)):
            if stones[i] in strArr:
                count += 1
        return count