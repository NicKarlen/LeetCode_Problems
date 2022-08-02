from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.prev = float("-inf")
        self.inorder(root)
        return self.flag

        
    def inorder(self,root):
        #base condition
        if root==None:
            return
        

        self.inorder(root.left)
        
        if root.val<=self.prev:
            self.flag = False            
        self.prev = root.val
        
        self.inorder(root.right)




sl = Solution()


# root = TreeNode(val= 5, left= TreeNode(val= 3,     left= TreeNode(val= 2), 
#                                                     right= TreeNode(val= 4)), 
#                         right= TreeNode(val= 10,    left= TreeNode(val= 4), 
#                                                     right= TreeNode(val= 12)))

root = TreeNode(val= 32, left= TreeNode(val= 26,     left= TreeNode(val= 19, right=TreeNode(val=27))), 
                        right= TreeNode(val= 47,    right= TreeNode(val= 56)))

print(sl.isValidBST(root))





        # while nodedeque:
        #     # For each level we go trow all nodes.
        #     levelLen = len(nodedeque) 
        #     for i in range(levelLen): 
        #         cur = nodedeque.popleft()
        #         if cur.left:
        #             if cur.left.val < cur.val:
        #                 nodedeque.append(cur.left)
        #             else:
        #                 return False
        #         if cur.right:
        #             if cur.right.val > cur.val:
        #                 nodedeque.append(cur.right)
        #             else:
        #                 return False

        # return True


    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     from collections import deque

    #     nodedeque = deque([root])
    #     treepath = 'left'
    #     rightpath_node = None
    #     first = True
    #     last_right = -2**32
    #     last_left = root.val

    #     # As long as we find new nodes we stay in the while loop. (This way of going throw a binary three is called BFS.)
    #     while nodedeque:
    #         # For each level we go trow all nodes.
    #         levelLen = len(nodedeque) 
    #         for i in range(levelLen): 
    #             cur = nodedeque.popleft()
    #             print(cur.val)
    #             if rightpath_node == cur:
    #                 last_right = root.val
    #                 last_left = 2**32
            
    #             if cur.right:
    #                 if first:
    #                     rightpath_node = cur.right

    #                 if cur.right.val < last_left and cur.right.val > last_right:
    #                     nodedeque.appendleft(cur.right)        
    #                     last_right                    
    #                 else:
    #                     return False
    #             if cur.left:
    #                 if cur.right.val < last_left and cur.right.val > last_right:
    #                     nodedeque.appendleft(cur.left)
    #                 else:
    #                     return False
    #             first = False
    #     return True
