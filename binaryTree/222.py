# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 遍历
        # 递归遍历
        def InOrder(root):
            count = 0
            if root == None:
                return 0
            else:
                count += 1
            count += InOrder(root.left)
            count += InOrder(root.right)

            return count
        return InOrder(root)