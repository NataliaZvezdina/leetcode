# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        base_length, remainder = divmod(length, k)
    
        cur = head
        res = []
        for i in range(k):
            res.append(cur)
            for j in range(base_length + (1 if remainder else 0) - 1):
                if not cur: break
                cur = cur.next
            remainder -= (1 if remainder else 0)
            if cur:
                cur.next, cur = None, cur.next

        return res
        