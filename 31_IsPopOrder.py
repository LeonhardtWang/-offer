# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while True:
            if not stack or stack[-1] != popV[0]:
                stack.append(pushV.pop(0))
            else:
                stack.pop()
                popV.pop(0)
            if not popV:return True
            if not pushV and (stack[-1] != popV[0]):
                return False