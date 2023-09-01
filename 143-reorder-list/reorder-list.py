# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = slow.next = None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        one, two = head, prev
        while two:
            tmp1, tmp2 = one.next, two.next
            one.next = two
            two.next = tmp1
            one, two = tmp1, tmp2