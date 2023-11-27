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
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        one, two = head, prev
        while two:
            tm1, tm2 = one.next, two.next
            one.next = two
            two.next = tm1
            one, two = tm1, tm2
        
