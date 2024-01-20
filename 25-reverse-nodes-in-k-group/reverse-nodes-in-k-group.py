# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                cur.next, cur, prev = prev, cur.next, cur
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next


    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

















    #     dummy = ListNode(0, head)
    #     groupPrev = dummy
        
    #     while True:
    #         kth = self.getKth(groupPrev, k)
    #         if not kth:
    #             break
    #         groupNext = kth.next

    #         prev, curr = kth.next, groupPrev.next
    #         while curr != groupNext:
    #             curr.next, prev, curr = prev, curr, curr.next

    #         temp = groupPrev.next
    #         groupPrev.next = kth
    #         groupPrev = temp
    #     return dummy.next

    # def getKth(self, curr, k):
    #     while curr and k > 0:
    #         curr = curr.next
    #         k -= 1
    #     return curr