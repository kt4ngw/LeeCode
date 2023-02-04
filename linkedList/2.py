# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        while (l1 != None):
            arr1.append(l1.val)
            l1 = l1.next
        while (l2 != None):
            arr2.append(l2.val)
            l2 = l2.next
        arrLenTemp = len(arr1) - 1
        num1 = 0
        num2 = 0
        for i in range(len(arr1) - 1, -1, -1):
            num1 += arr1[i] * (10 ** arrLenTemp)
            arrLenTemp -= 1
        arrLenTemp = len(arr2) - 1
        for i in range(len(arr2) - 1, -1, -1):
            num2 += arr2[i] * (10 ** arrLenTemp)
            arrLenTemp -= 1
        num = num1 + num2
        arr = []
        if num == 0:
            arr.append(0)
        else:
            while (num != 0):
                arr.append(num % 10)
                num = num // 10
        c = ListNode()
        c = ListNode(arr[0])
        head = c
        for i in range(1, len(arr)):
            c.next = ListNode(arr[i])
            c = c.next
        return head