#Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
#
# Example: 
#
# 
#Given nums = [2, 7, 11, 15], target = 9,
#
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#
# Related Topics Array Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
#leetcode submit region end(Prohibit modification and deletion)

    def twoSum2(self, nums, target):  # no type hints is also right
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

    def twoSum4(self, nums: List[int], target: int) -> List[int]:  # O(n^2)
        for i in nums:
            j = target - i
            tmp_nums_start_index = nums.index(i) + 1
            tmp_nums = nums[tmp_nums_start_index:]
            if j in tmp_nums:
                return [nums.index(i), tmp_nums_start_index + tmp_nums.index(j)]
    # twoSum(self, [2, 7, 11, 15], 9) # wrong method invocation


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum3([2, 7, 11, 15], 9))
