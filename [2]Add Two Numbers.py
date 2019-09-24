#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. 
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
#
# Example: 
#
# 
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
# 
# Related Topics Linked List Math



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur, carry = dummy, 0

        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            # 1st way
            cur.next = ListNode(carry % 10)
            carry //= 10  # Truncation Division (also known as floor division)
            cur = cur.next  # important

            # 2nd way
            # carry, val = divmod(carry, 10)
            # cur.next = ListNode(val)
            # cur = cur.next

        if carry == 1:
            cur.next = ListNode(1)

        return dummy.next
        
#leetcode submit region end(Prohibit modification and deletion)
