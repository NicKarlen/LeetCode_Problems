import enum
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"val: {self.val}; next(val): {self.next.val}"
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # arr = []
        # while True:
        #     try:
        #         if list1.val > list2.val:
        #             arr.append(list2.val)
        #             list2 = list2.next
        #         else:
        #             arr.append(list1.val)
        #             list1 = list1.next
        #     except:
        #         if list1 != None:
        #             arr.append(list1.val)
        #             list1 = list1.next     
        #         elif list2 != None:
        #             arr.append(list2.val)
        #             list2 = list2.next
        #         else:
        #             break                                   

        # res = ListNode(val=arr[-1])
        # arr.pop()
        # for i in reversed(arr):
        #     res = ListNode(val=i,next=res)
        # return res

        """
            dummy acts as a pointer to the first ListNode in the chain. We need it to be able to point to it when we return the chain of ListNode.

            https://stackoverflow.com/questions/58759348/when-does-a-pointer-to-a-linked-list-change-the-actual-list 
        """
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next


sl = Solution()

ln1 = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=4)))

ln2 = ListNode(val=1,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5))))

print(sl.mergeTwoLists(ln1, ln2))