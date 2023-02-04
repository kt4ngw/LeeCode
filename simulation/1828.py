class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for circle in queries: #  [[2,3,1],[4,3,1],[1,1,2]]
            # 遍历⚪
            count = 0
            for point in points: # [[1,3],[3,3],[5,3],[2,2]]
                # 遍历点
                # 判断点到圆心的距离会不会小于等于半径
                if ((point[0] - circle[0]) ** 2 + (point[1] - circle[1]) ** 2 <= circle[2] ** 2):
                    count += 1
            res.append(count)
        return res

