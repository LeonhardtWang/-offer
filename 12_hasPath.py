# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        flag = [0] * len(matrix)
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    res = self.find(flag, matrix, rows, cols, path[1:], i, j)
                    if res == True:
                        return True
                    else:
                        flag[i*cols+j] = 0
        return False
    
    def find(self, flag, matrix, rows, cols, path, i, j):
        flag[i*cols+j] = 1
        if not path:
            return True
        if i - 1 >= 0 and matrix[(i-1)*cols+j] == path[0] and flag[(i-1)*cols+j] == 0:
            res = self.find(flag, matrix, rows, cols, path[1:], i-1, j)
            if res == True:
                return res
            else:
                flag[(i-1)*cols+j] = 0
        if i + 1 <= rows - 1 and matrix[(i+1)*cols+j] == path[0] and flag[(i+1)*cols+j] == 0:
            res = self.find(flag, matrix, rows, cols, path[1:], i+1, j)
            if res == True:
                return res
            else:
                flag[(i+1)*cols+j] = 0
        if j - 1 >= 0 and matrix[i*cols+j-1] == path[0] and flag[i*cols+j-1] == 0:
            res = self.find(flag, matrix, rows, cols, path[1:], i, j-1)
            if res == True:
                return res
            else:
                flag[i*cols+j-1] = 0
        if j + 1 <= cols - 1 and matrix[i*cols+j+1] == path[0] and flag[i*cols+j+1] == 0:
            res = self.find(flag, matrix, rows, cols, path[1:], i, j+1)
            if res == True:
                return res
            else:
                flag[i*cols+j+1] = 0
        return False


if __name__ == "__main__":
    solution = Solution()
    res = solution.hasPath("ABCESFCSADEE",3,4,"SEE")
    print(res)