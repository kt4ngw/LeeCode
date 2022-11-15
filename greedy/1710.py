class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 先将第二列从大到小排序（排序时间复杂度，快排？）
        # 高效排序 + 贪心

        # 排序
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        result = 0
        # 贪心
        for box in boxTypes:
            if box[0] <= truckSize:
                truckSize = truckSize - box[0]
                result = result + box[0] * box[1]
            else:
                result = result + truckSize * box[1]
                break

        return result

        # res = 剩下需要的箱子