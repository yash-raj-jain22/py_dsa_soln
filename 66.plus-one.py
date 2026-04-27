#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a="".join(map(str, digits))
        a=int(a)+1
        a=str(a)
        a1 = list(map(lambda x: int(x), a))
        return a1
    
# @lc code=end

