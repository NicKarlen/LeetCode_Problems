# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findPath(root, path, k):
        
            # Baes Case
            if root is None:
                return False
        
            # Store this node is path vector. The node will be
            # removed if not in path from root to k
            path.append(root.val)
        
            # See if the k is same as root's val
            if root.val == k :
                return True
        
            # Check if k is found in left or right sub-tree
            if ((root.left != None and findPath(root.left, path, k)) or
                    (root.right!= None and findPath(root.right, path, k))):
                return True
        
            # If not present in subtree rooted with root, remove
            # root from path and return False
            
            path.pop()
            return False
        

        # To store paths to n1 and n2 fromthe root
        path1 = []
        path2 = []
    
        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        if (not findPath(root, path1, p.val) or not findPath(root, path2, q.val)):
            return -1
    
        # Compare the paths to get the first different value
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]




sl = Solution()


root = TreeNode(val= 3, left= TreeNode(val= 9,     left= TreeNode(val= 98), 
                                                    right= TreeNode(val= 99)), 
                        right= TreeNode(val= 20,    left= TreeNode(val= 15), 
                                                    right= TreeNode(val= 7)))

p = TreeNode(val= 99)

q = TreeNode(val= 20,    left= TreeNode(val= 15), right= TreeNode(val= 7))

print(sl.lowestCommonAncestor(root, p, q ))



        # from collections import deque

        # nodedeque = deque([root])
        # history_p = []
        # p_found = False
        # history_q = []
        # q_found = False
        # start = True
        # midpoint_reached = False
        # while nodedeque:
        #     cur = nodedeque.popleft()
        #     print(len(nodedeque))
        #     if not start and not midpoint_reached and len(nodedeque) == 0:
        #         if not p_found:
        #             history_p = [root]
        #         if not q_found:
        #             history_q = [root]
        #         midpoint_reached = True
        #     start = False

        #     if not p_found:
        #         history_p.append(cur)
        #     if not q_found:
        #         history_q.append(cur)

        #     if cur.val == p.val:
        #         p_found = True
        #     if cur.val == q.val:
        #         q_found = True

        #     print(cur.val)

        #     if cur.right:
        #         nodedeque.appendleft(cur.right)
        #     if cur.left:   
        #         nodedeque.appendleft(cur.left)

        

        # return True