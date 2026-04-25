#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count =0
        nums1=[]
        for i in range(len(nums)):
            if nums[i] == val:
                nums1.append(i)
        for i in (nums1):
            nums.pop(i-count)
            count+=1
        return len(nums)
# @lc code=end

