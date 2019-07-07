# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n > len(s):
            return s
        s_list = list(s)
        self.Reverse(s_list, 0, n-1)
        self.Reverse(s_list, n, len(s_list)-1)
        self.Reverse(s_list, 0, len(s_list)-1)
        return ''.join(s_list)
        
    
    def Reverse(self, s_list, pBegin, pEnd):
        while pBegin < pEnd:
            temp = s_list[pBegin]
            s_list[pBegin] = s_list[pEnd]
            s_list[pEnd] = temp
            pBegin += 1
            pEnd -= 1
        

if __name__ == "__main__":
    print(Solution().LeftRotateString('abcdeft', 2))