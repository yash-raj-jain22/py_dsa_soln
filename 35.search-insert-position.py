#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        t=-1
        for i in range(1,len(nums)):
                # continue
            if nums[i-1]<target<=nums[i]:
                t=i
                break
            elif nums[i-1]>=target:
                t=i-1
                break
                # break
        if len(nums)==1 and nums[0]>=target:
            t=0
        elif len(nums)==1 and nums[0]<target:
            t=1
        if t==-1:
            t=len(nums)
        return int(t)
# @lc code=end

