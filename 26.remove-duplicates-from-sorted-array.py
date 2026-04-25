#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp =[]
        count=0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                temp.append(i)
        for i in temp:
            nums.pop(i-1-count)
            count+=1
        return len(nums)
# @lc code=end

