# -*- coding:utf-8 -*-
class Solution:
    def isEven(self, n):
        if n & 1 == 1:
            return False
        else:
            return True
    def reOrderArray(self, array):
        # write code here
        
        '''
        注意保证相对位置不变
        if len(array) <= 1:return array
        head_index = 0;last_index = len(array) - 1
        while head_index  < last_index:
            res_head = self.isEven(array[head_index])
            res_last = self.isEven(array[last_index])
            if not res_head:head_index += 1
            if res_last:last_index -= 1
            if res_head and not res_last:
                temp = array[head_index]
                array[head_index] = array[last_index]
                array[last_index] = temp
                head_index += 1; last_index -= 1
        return array
        '''
        # 类似冒泡法，每次总能冒泡一个到列表最左端，且不影响相对位置
        for i in range(len(array)-1):
            for j in range(len(array)-1, i, -1):
                if self.isEven(array[j-1]) and not self.isEven(array[j]):
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
                    

print(Solution().reOrderArray([1, 2, 3, 4, 5, 6, 7]))