# -*- coding:utf-8 -*-
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 分三步
        # 第一步：根据原始链表中每个节点N创建对应的N',把N'链接在N后面
        # 第二步：设置复制出来的节点的.random
        # 第三步：把偶数节点链接起来即是结果
        
        # 第一步
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pCloned.random = None
            
            pNode.next = pCloned
            pNode = pCloned.next
            
        # 第二步
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
            
        # 第三步
        pNode = pHead
        pClonedHead = None
        pClonedNode = None
        
        if pNode:
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
            
        return pClonedHead