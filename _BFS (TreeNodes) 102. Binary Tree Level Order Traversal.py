
from typing import Optional

# Definition for a binary tree node.

"""
    Binary Trees: 
    
    Binärbäume sind in der Informatik die am häufigsten verwendete Unterart der Bäume.
    Im Gegensatz zu anderen Arten von Bäumen können die Knoten eines Binärbaumes 
    nur höchstens zwei direkte Nachkommen haben. Meist wird verlangt, dass sich die 
    Kindknoten eindeutig in linkes und rechtes Kind einteilen lassen.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:

        """
            My Solution:
        """
        # cur = root
        # res = []
        # history = []
        # back = False
        # level = 0

        # while cur:
        #     if back == False:
        #         try:
        #             res[level].append(cur.val)
        #         except:
        #             res.append([cur.val])

        #     back = False
        #     history.append(cur)

        #     if cur.left:
        #         cur = cur.left 
        #         level += 1
        #         history[-1].left = None
        #     elif cur.right:
        #         cur = cur.right
        #         level += 1
        #         history[-1].right = None
        #     else:
        #         try:
        #             level -= 1
        #             history.pop()
        #             cur = history.pop()
        #             back = True
        #         except:
        #             return res
            
        """
            Better Solution:

            Ich gehe Level um Level durch und schreibe mir immer die gefundenen .left und anschliessend .right in einem array auf und arbeite sie dann von vorne ab..

            Ein Deque (Double-ended queue). Wir fügen hinten an und nehmen vorne weg... BFS = Breadth-first search

        """
        from collections import deque
        # Corner case.
        if not root:
            return []
        
        nodes = []  # Result nodes.
        nodeDeque = deque([root])  
        # BFS on tree using nodeDeque.
        while nodeDeque:
            levelLen = len(nodeDeque)
            levelNodes = []
            for i in range(levelLen):
                curNode = nodeDeque.popleft()
                levelNodes.append(curNode.val)
                if curNode.left:
                    nodeDeque.append(curNode.left)
                if curNode.right:
                    nodeDeque.append(curNode.right)  
            nodes.append(levelNodes)
            
        return nodes

sl = Solution()


root = TreeNode(val= 3, left= TreeNode(val= 9,     left= TreeNode(val= 98), 
                                                    right= TreeNode(val= 99)), 
                        right= TreeNode(val= 20,    left= TreeNode(val= 15), 
                                                    right= TreeNode(val= 7)))

print(sl.levelOrder(root))