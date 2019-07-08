# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.num_lis = []
        
    def Insert(self, num):
        # write code here
        self.num_lis.append(num)
        self.num_lis.sort()
            
    def GetMedian(self, num_lis):
        # write code here
        mid = len(self.num_lis) // 2
        if len(self.num_lis) % 2 == 1:
            return self.num_lis[mid]
        else:
            return (self.num_lis[mid-1] + self.num_lis[mid]) / 2


if __name__ == "__main__":
    lis = [5,2,3,4,1,6,7,0,8]
    solution = Solution()
    for num in lis:
        solution.Insert(num)
        print(solution.num_lis)
        print(solution.GetMedian(None))