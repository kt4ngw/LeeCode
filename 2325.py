class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # 哈希表 ，键值对一一对应
        result = ''
        dic = dict()
        count = 97 # 对哈希表键值对的值进行初始赋值 字母a的ACSII等于97
        for i in range(len(key)):
            if key[i] != ' ' and key[i] not in dic:
                dic[key[i]] = chr(count)
                count += 1 # 字母a 存放完，加1存放字母b
        # 此时哈希表26个字母一一对应
        for i in range(len(message)):
            if message[i] == ' ':
                result += ' '
            else:
                result += dic[message[i]]
        return result