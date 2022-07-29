class Solution:
    def search(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


sl = Solution()


print(sl.search(nums = [-1,0,3,5,9,12], target = 9))



"""
    This was the idea of the exercise:
    https://leetcode.com/problems/binary-search/solution/ 
    

"""