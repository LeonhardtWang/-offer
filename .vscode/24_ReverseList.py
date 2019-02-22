# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        temp = None
        ptr_pre, ptr_last = pHead, pHead

        while ptr_last:
            ptr_last = ptr_last.next
            ptr_pre.next = temp
            temp = ptr_pre
            ptr_pre = ptr_last
        return temp
            