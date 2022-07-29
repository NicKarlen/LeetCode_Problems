class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num > 0:
            if num % 2:
                num = num -1
            else:
                num = num/2
            res += 1
        return res

sl = Solution()

print(sl.numberOfSteps(123))