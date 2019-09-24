#Given a string, find the length of the longest substring without repeating characters. 
#
# 
# Example 1: 
#
# 
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
# 
#
# 
# Example 2: 
#
# 
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
# 
#
# 
# Example 3: 
#
# 
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
# 
# 
# Related Topics Hash Table Two Pointers String Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0  # can't be initialized to -sys.maxsize since corner case: empty string
        d = {}
        r = 0
        for l in range(len(s)):
            while r < len(s) and (not s[r] in d.keys() or d[s[r]] < 1):
                d[s[r]] = 1
                r += 1

            res = max(res, r - l)
            d[s[l]] = 0

        return res        
#leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.lengthOfLongestSubstring("ddabca"))
