class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split(" ")
        result = ''
        for i in range(len(wordList) - 1, -1, -1):
            if len(wordList[i]) > 0:
                result += wordList[i] + ' '

        return result[:len(result) - 1]