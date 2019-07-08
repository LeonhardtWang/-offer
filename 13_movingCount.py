# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        
        visited = [False] * rows * cols
        
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        
        del visited
        return count
    
    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row*cols+col] = True
            count = (1 + self.movingCountCore(threshold, rows, cols, row-1, col, visited)
                       + self.movingCountCore(threshold, rows, cols, row, col-1, visited)
                       + self.movingCountCore(threshold, rows, cols, row+1, col, visited)
                       + self.movingCountCore(threshold, rows, cols, row, col+1, visited)
                    )
        return count
    
    def check(self, threshold, rows, cols, row, col, visited):
        if (row >= 0 and row < rows and col >= 0 and col < cols
            and self.getDigitSum(row) + self.getDigitSum(col) <= threshold
            and visited[row*cols+col] == False):
            return True
        return False
    
    def getDigitSum(self, number):
        number = int(number)
        sum_ = 0
        while number > 0:
            sum_ += number % 10
            number //= 10
        return sum_


if __name__ == "__main__":
    solution = Solution()
    res = solution.movingCount(10,1,10)
    print(res)