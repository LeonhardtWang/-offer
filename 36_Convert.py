# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        left = pRootOfTree.left
        right = pRootOfTree.right
        
        if not left and not right:
            return pRootOfTree
        
        left = self.Convert(left)
        right = self.Convert(right)
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left = left
            left.right = pRootOfTree
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree
        
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

        