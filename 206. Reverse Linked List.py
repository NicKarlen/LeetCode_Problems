from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"val: {self.val}; next(val): {self.next.val}"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nl = None
        while head:
            nl = ListNode(val=head.val, next=nl)
            head = head.next
         
        return nl

sl = Solution()

ln2 = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5,next=ListNode(val=6))))))


sl.reverseList(ln2)