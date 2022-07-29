from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        h = head
        li = []
        while True:
            li.append(h.val)
            if h.next == None:
                break
            else:
                h = h.next

        print(li)
        while True:
            if len(li) >= 2:
                if li.pop(0) != li.pop():
                    return False
                print(li)
            else:
                return True
        

ln = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=2,next=ListNode(val=1,next=ListNode(val=2,next=ListNode(val=2,next=ListNode(val=1)))))))


sol = Solution()

print(sol.isPalindrome(ln))