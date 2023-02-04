# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def isPalind(arr):
            left = 0
            right = len(arr) - 1
            flag = 1
            while (left <= right):
                if arr[left] != arr[right]:
                    flag = 0
                    break
                left += 1
                right -= 1
            return True if flag == 1 else False

        arr = []
        while (head != None):
            arr.append(head.val)
            head = head.next
        return isPalind(arr)
