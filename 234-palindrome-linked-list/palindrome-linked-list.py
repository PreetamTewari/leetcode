# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        cur = head
        while cur:
            li.append(cur.val)
            cur = cur.next

        l, r = 0, len(li) - 1
        while l < r:
            if li[l] != li[r]:
                return False
            l += 1
            r -= 1
        return True