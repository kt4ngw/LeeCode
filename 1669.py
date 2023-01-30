# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ## 简单模拟
        virtualNode = ListNode(-1, )
        virtualNode.next = list1
        i = virtualNode
        j = virtualNode
        while (a != 0):
            i = i.next
            a -= 1
        while (b != -1):
            j = j.next
            b -= 1
        i.next = list2

        while (list2.next != None):
            list2 = list2.next
        list2.next = j.next
        return virtualNode.next