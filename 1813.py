class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        # 双指针
        if len(sentence1) > len(sentence2):
            shortStr = sentence2
            longStr = sentence1
        else:
            shortStr = sentence1
            longStr = sentence2
        shortList = shortStr.split(' ')
        longList = longStr.split(' ')
        i = 0
        j = 0
        while(i < len(shortList) and shortList[i] == longList[i]):
            i += 1
        while(len(shortList) - j > i and shortList[len(shortList) - 1 - j] == longList[len(longList) - 1 - j]):
            j += 1
        if(i + j == len(shortList)):
            return True
        else:
            return False