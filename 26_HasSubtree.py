# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def equal(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1 and pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            return self.equal(pRoot1.left, pRoot2.left) & self.equal(pRoot1.right, pRoot2.right)
        else:
            return False
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:return False
        if self.equal(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)