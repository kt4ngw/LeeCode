# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 # 链表的长度
        i = head # 用临时指针i扫描一边链表长度
        while(i != None):
            length += 1
            i = i.next

        virtualNode = ListNode() # 创建一个虚拟头节点
        virtualNode.next = head
        # 去掉第几个
        pointLeft = virtualNode
        i = 0
        while(i < length - n): # 根据数学关系，下标和长度找到对应遍历的值
            pointLeft = pointLeft.next
            i += 1


        pointLeft.next = pointLeft.next.next # 换指针
        return virtualNode.next # 输出虚拟结点的next

## 暂时非进阶 进阶说只要一趟扫描
