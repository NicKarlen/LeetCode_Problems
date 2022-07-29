class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_order = []
        pos = 0
        pos_old = 0
        for char in s:
            pos = t.find(char)
            if pos >= 0:
                char_order.append(pos+pos_old)
                t = t[pos+1:]
                pos_old += pos+1
            else:
                return False
                
        if char_order != sorted(char_order):
            return False
        return True

sl = Solution()

print(sl.isSubsequence('axc','ahhgfdc'))

