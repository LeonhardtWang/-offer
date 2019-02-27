# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        m, n = len(matrix), len(matrix[0])
        for i in matrix[0]:
            res.append(i)
        if m == 1:return res
        new_matrix = []
        for i in range(1, n+1):
            new_matrix.append([matrix[j][-i] for j in range(1, m)])
        return res + self.printMatrix(new_matrix)