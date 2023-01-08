class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # 遍历
        prefLen = len(pref)
        count = 0 # 计数有多少个单词符合
        for word in words:
            if prefLen > len(word):
                continue #特殊情况 给定的前缀 大于单词的长度
            else:
                flag = 1
                for j in range(prefLen):
                    if pref[j] != word[j]:
                        flag = 0
                        break
                if flag == 1:
                   count += 1
        return count