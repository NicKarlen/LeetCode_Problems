from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        li = []
        while h:
            li.append(h.val)
            h = h.next
        print(li)
        def get_node(index: int):
            h = head
            while index > 0:
                h = h.next
                index = index - 1

            return h

        if len(li) % 2 == 0:
            return get_node(int(len(li)/2 + 0.5))
        else:
            return get_node(int(len(li)/2))


#ln = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=2,next=ListNode(val=1,next=ListNode(val=2,next=ListNode(val=2,next=ListNode(val=1)))))))
ln = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5,next=ListNode(val=6,next=ListNode(val=7)))))))

sol = Solution()

print(sol.middleNode(ln).val)