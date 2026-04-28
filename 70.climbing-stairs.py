#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n%2==0:
            return int((n/2)+1)
        else:
            return int(((n-1)/2)+1)
# @lc code=end

