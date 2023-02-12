class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 模拟
        locate = [0, 0]
        locateFind = [-1, -1]
        result = ''
        for i in range(len(target)):
            # locateFind 需要找的位置
            tempNum = (ord(target[i]) - 97)
            locateFind[0] = tempNum // 5
            locateFind[1] = tempNum % 5
            # 需要处理特殊情况 Z
            while locateFind[0] - locate[0] < 0:  # 如果要寻找的位置在当前位置的上面
                result += 'U'
                locate[0] -= 1
            while locateFind[1] - locate[1] < 0:  # 如果要寻找的位置在当前位置的左面
                result += 'L'
                locate[1] -= 1
            while locateFind[0] - locate[0] > 0:  # 如果要寻找的位置在当前位置的下面
                result += 'D'
                locate[0] += 1
            while locateFind[1] - locate[1] > 0:  # 如果要寻找的位置在当前位置的右面
                result += 'R'
                locate[1] += 1
            result += '!'
        return result

