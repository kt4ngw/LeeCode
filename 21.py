# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个结点 首先指向Null
        point = ListNode()
        pointD = point
        while(True):
            if(list1 == None or list2 == None):
                break
            if(list1.val <= list2.val):
                pointD.next = list1
                list1 = list1.next
                pointD =  pointD.next
            else:
                pointD.next = list2
                list2 = list2.next
                pointD =  pointD.next

        while(list1 != None):
                pointD.next = list1
                list1 = list1.next
                pointD =  pointD.next
        while(list2 != None):
                pointD.next = list2
                list2 = list2.next
                pointD =  pointD.next
        return point.next