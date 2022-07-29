class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        x_sum = 0
        for i in range(0,len(nums)):
            x_sum = x_sum + nums[i]
            res.append(x_sum)
        return res
        """
        Bottom is slower
        """
        # res = []
        # x_sum = 0
        # for num in nums:
        #     x_sum = x_sum + num
        #     res.append(x_sum)
        # return res


sl = Solution()

print(sl.runningSum([1,2,3,4]))