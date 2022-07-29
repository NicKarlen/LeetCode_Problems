from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"val: {self.val}; next(val): {self.next.val}"

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)

        return arr[len(arr) // 2]


#ln = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=2,next=ListNode(val=1,next=ListNode(val=2,next=ListNode(val=2,next=ListNode(val=1)))))))
ln = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5,next=ListNode(val=6,next=ListNode(val=7, next=ListNode(val=8))))))))

sol = Solution()

print(sol.middleNode(ln))