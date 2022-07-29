# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pivot = left + (right - left) // 2
            bad = self.isBadVersion(pivot)
            if bad == True:
                if self.isBadVersion(pivot-1) == False:
                    return pivot
                right = pivot - 1
            else:
                left = pivot + 1


    def isBadVersion(self, n):
        if n >= 5:
            return True
        else:
            return False


sl = Solution()

print(sl.firstBadVersion(8))