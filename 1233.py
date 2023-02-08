class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        # 维护一个基字符串，如果遍历的字符串前缀和及字符一样且下一个字符是"/"，那么就是子文件夹，如果前缀不一样，那么就换一个基字符串，并把改字符串加入到结果当中
        for i in range(len(folder)):
            if i == 0: 
                base = folder[i]
                baseLen = len(base)
                result.append(base)
                continue
            if folder[i][0:baseLen] == base and folder[i][baseLen] == '/':    
                continue
            else:
                result.append(folder[i])
                base = folder[i]
                baseLen = len(base)
        return result