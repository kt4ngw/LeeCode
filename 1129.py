n = 3
redEdges = [[0,1],[1,2]]
blueEdges = [[0,1],[1,2]]
#
#
# class Solution:
#     def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
#         g = [[] for _ in range(n)]
#         for x, y in redEdges:
#             g[x].append((y, 0))
#         for x, y in blueEdges:
#             g[x].append((y, 1))
#
#         dis = [-1] * n
#         vis = {(0, 0), (0, 1)}
#         q = [(0, 0), (0, 1)]
#         level = 0
#         while q:
#             tmp = q
#             q = []
#             for x, color in tmp:
#                 if dis[x] == -1:
#                     dis[x] = level
#                 for p in g[x]:
#                     if p[1] != color and p not in vis:
#                         vis.add(p)
#                         q.append(p)
#             level += 1
#         return dis
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/shortest-path-with-alternating-colors/solution/yan-se-jiao-ti-de-zui-duan-lu-jing-by-le-vnuu/
# 来源：力扣（LeetCode）

from queue import Queue

g = [[] for _ in range(n)]
for x, y in redEdges:
    g[x].append((y, 0))
for x, y in blueEdges:
    g[x].append((y, 1))
print(g[0])
result = [-1] * n
result[0] = 0
visit = {g[0][0]}
height = 0
q = Queue()
q.put(g[0])
while (q.qsize() != 0):
    for i, color in q.get():
        if result[i] == -1:
            result[i] = height
        for j in g[i]:
            if j[1] != color and j not in visit:
                visit.add(j)
                q.put(j)
    height = height + 1
print(result)