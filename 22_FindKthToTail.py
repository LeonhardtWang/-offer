# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0 or not head:return None
        ptr_fast = head
        while k != 0:
            ptr_fast = ptr_fast.next
            k -= 1
            if not ptr_fast and k != 0:
                return None
        ptr_slow = head
        while ptr_fast:
            ptr_fast = ptr_fast.next
            ptr_slow = ptr_slow.next
        return ptr_slow
            