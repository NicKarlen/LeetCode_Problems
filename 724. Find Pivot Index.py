class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # def running_sum(start: int, end:int, step:int):
        #     res = []
        #     x_sum = 0
        #     for i in range(start,end,step):
        #         x_sum = x_sum + nums[i]
        #         if start < end:
        #             res.append(x_sum)
        #         else:
        #             res.insert(0,x_sum)
        #     return res

        # x = running_sum(0,len(nums),1)
        # y = running_sum(len(nums)-1,-1,-1)

        # for i in range(len(nums)):
        #     if x[i] == y[i]:
        #         return i
        # return -1
        leftsum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            if leftsum == (total - leftsum - num):
                return i
            else:
                leftsum += num
        return -1
sl = Solution()

print(sl.pivotIndex([1,7,3,6,5,6]))