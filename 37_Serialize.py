# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 输入列表，生成二叉树
def binary_trees(input):
    if not input:return None
    root = TreeNode(input[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input):
        node = nodeQueue[front]
        front += 1

        item = input[index]
        index += 1
        if item != 'null':
            node.left = TreeNode(item)
            nodeQueue.append(node.left)
        
        if index >= len(input):break
        
        item = input[index]
        index += 1
        if item != 'null':
            node.right = TreeNode(item)
            nodeQueue.append(node.right)
    return root

class Solution:
    def __init__(self):
        self.i = 0
        
    def Serialize(self, root):
        # write code here
        if root is None:
            return '#'
        return (str(root.val) + ',' + self.Serialize(root.left)
                + ',' + self.Serialize(root.right))
    
    def Deserialize(self, s):
        # write code here
        s_lis = s.split(',')
        if s_lis[self.i] == '#' or self.i >= len(s_lis):
            return None
            self.i += 1
        root = TreeNode(int(s_lis[self.i]))
        self.i += 1
        root.left = self.Deserialize(s)
        root.right = self.Deserialize(s)
        return root

if __name__ == "__main__":
    root = binary_trees([8,6,10,5,7,9,11])
    solution = Solution()
    s = solution.Serialize(root)
    print(s)
    root = solution.Deserialize(s)