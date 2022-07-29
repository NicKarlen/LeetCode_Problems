from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        if not self:
            return None
        output = 'Index; val; next.val\n'
        node = self
        idx = 0
        while node:
            output += f"{idx};  {node.val}; {node.next.val if node.next else None}\n"
            idx += 1
            node = node.next
            if idx > 20:
                output += "!!-- more than 20 nodes --!!"
                break
        return output


ln1 = ListNode()
ln2 = ListNode(val=3,next=ListNode(val=2,next=ListNode(val=0,next=ListNode(val=-4))))


print(ln1, "\n")
print(ln2)