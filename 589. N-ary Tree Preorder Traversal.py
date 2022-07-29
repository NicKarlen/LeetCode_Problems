# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
    def __str__(self) -> str:
        x = 'nixx'
        return f"val: {self.val or x}; children: {self.children or x}"


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        cur = root
        res = []
        history = []
        back = False

        while cur:
            if back == False:
                res.append(cur.val)

            back = False
            history.append(cur)

            if cur.children:
                cur = cur.children.pop(0)
            else:
                try:
                    history.pop()
                    cur = history.pop()
                    back = True
                except:
                    return res

        
sl = Solution()

root = Node(val=1, children=[Node(val=3,children=[Node(val=5),Node(val=6)]), Node(val=2), Node(val=4)])

print(sl.preorder(root))