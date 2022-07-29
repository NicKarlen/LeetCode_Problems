class Solution:
    def longestPalindrome(self, s: str) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        letters = alpha + alpha.upper()

        res = 0
        one = False
        for letter in letters:
            count = s.count(letter)
            if count % 2 == 1:
                if one == False:
                    res += 1
                    one = True
                count -= 1
            if count % 2 == 0:
                res += count
        return res


sl = Solution()

print(sl.longestPalindrome('aaaaaaaaaaaaaaaaaaa'))