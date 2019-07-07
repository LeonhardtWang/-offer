# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_list = list(s)
        length = len(s_list)
        if length <= 1:
            return s
        self.Reverse(s_list, 0, length-1)
        
        pBegin = 0
        pEnd = 0
        while pEnd <= length:
            if s_list[pBegin] == ' ':
                pBegin += 1
                pEnd += 1
            elif pEnd == length or s_list[pEnd] == ' ':
                self.Reverse(s_list, pBegin, pEnd-1)
                pBegin = pEnd + 1
                pEnd += 1
            else:
                pEnd += 1
                
        return ''.join(s_list)
            
        
    def Reverse(self, s_list, pBegin, pEnd):
        while pBegin < pEnd:
            temp = s_list[pBegin]
            s_list[pBegin] = s_list[pEnd]
            s_list[pEnd] = temp
            pBegin += 1
            pEnd -= 1
            
            

if __name__ == "__main__":
    print(Solution().ReverseSentence(''))