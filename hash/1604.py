class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = dict()
        # 利用哈希表把对应的名字及其时间全部存储下来
        # 例如
        # """{"daniel":["10:00","10:40","11:00"], "luis":["11:00","13:00","15:00"]}"""
        # 然后查看每一个键值对的值 是否1小时三次便可
        def check(arr):
            # 如何检查这个列表?
            arr.sort()
            for i in range(len(arr) - 2):
                # 判断后两个时间减去当前时间是否都小于60？
                t1 = 0
                t2 = 0
                if (int(arr[i + 1][:2]) - int(arr[i][:2]) >= 1):
                    t1 += 60 * (int(arr[i + 1][:2]) - int(arr[i][:2]))
                else:
                    t1 += 0
                t1 += int(arr[i + 1][-2:]) - int(arr[i][-2:])
                if (int(arr[i + 2][:2]) - int(arr[i][:2]) >= 1):
                    t2 += 60 * (int(arr[i + 2][:2]) - int(arr[i][:2]))
                else:
                    t2 += 0
                t2 += int(arr[i + 2][-2:]) - int(arr[i][-2:])
                if (t1 <= 60) and (t2 <= 60):
                    return True
            return False

            return 
        for i in range(len(keyName)):
            if keyName[i] not in dic:
                dic[keyName[i]] = [keyTime[i]]
            else:
                dic[keyName[i]].append(keyTime[i])
        result = []
        for i in dic:
            if check(dic[i]): # 如果一小时三次卡
                result.append(i)
        result.sort()
        return result