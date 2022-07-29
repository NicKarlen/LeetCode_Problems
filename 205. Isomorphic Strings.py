class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        matches = {}
        used_chars = []
        for i,char in enumerate(s_list):
            if char in matches:
                if matches[char] != t_list[i] :
                    return False
            elif t_list[i] in used_chars:
                return False
            else:
                matches[char] = t_list[i]
                used_chars.append(t_list[i])
        return True

        

sl = Solution()

print(sl.isIsomorphic('badc','baba'))