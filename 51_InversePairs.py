# -*- coding:utf-8 -*-
from copy import deepcopy


class Solution:
    def InversePairs(self, data): 
        # write code here
        length = len(data)
        if not data or length < 0:
            return 0
        
        helper = deepcopy(data)
        count = self.InversePairsCore(data, helper, 0, length-1)
        del helper
        return count
        
    def InversePairsCore(self, data, helper, start, end):
        if start == end:
            helper[start] = data[start]
            return 0
        length = (end - start) // 2
        
        left = self.InversePairsCore(helper, data, start, start+length)
        right = self.InversePairsCore(helper, data, start+length+1, end)
        
        i = start + length
        j = end
        indexhelper = end
        count = 0
        
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                helper[indexhelper] = data[i]
                indexhelper -= 1
                i -= 1
                count = count + j - start - length
            else:
                helper[indexhelper] = data[j]
                indexhelper -= 1
                j -= 1
        while i >= start:
            helper[indexhelper] = data[i]
            indexhelper -= 1
            i -= 1
        while j >= start + length + 1:
            helper[indexhelper] = data[j]
            indexhelper -= 1
            j -= 1
        return left + right + count


if __name__ == "__main__":
    a = [627126,415347,850134,371085,279048,705820,453064,944751]
    print(Solution().InversePairs(a))