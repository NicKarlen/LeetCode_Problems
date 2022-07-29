from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"val: {self.val}; next(val): {self.next.val}"

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head.next == head.next.next.next.next) -> True!!
        head_arr = []
        h = head
        if not h:
            return None
        if not h.next:
            return None
        while h not in head_arr:
            head_arr.append(h)
            try:
                h = h.next
            except:
                return None
        return h


sl = Solution()

ln2 = ListNode(val=3,next=ListNode(val=2,next=ListNode(val=0,next=ListNode(val=-4))))
ln2.next.next.next.next = ln2

print(sl.detectCycle(ln2))