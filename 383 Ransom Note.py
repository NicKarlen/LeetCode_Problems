class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rN = list(ransomNote)
        mg = list(magazine)
        print(rN)
        print(mg)

        for ele in rN:
            if ele in mg:
                mg.remove(ele)
            else:
                return False
        
        return True

sol = Solution()

print(sol.canConstruct('abheyi','aabbiieeh'))