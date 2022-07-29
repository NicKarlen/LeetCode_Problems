class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        totals = []
        for acc in accounts:
            totals.append(sum(acc))
        return max(totals)

sl = Solution()

print(sl.maximumWealth([[1,2,3],[3,2,1]]))