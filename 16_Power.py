# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        '''
        不知该怎么处理负号数的情况
        if base == 0:return 0
        if exponent == 1:return 1
        res = self.Power(base, exponent >> 1)
        if exponent & 1 == 0:
            return res * res
        else:
            return res * res * base
        '''
        if base == 0:return 0
        res = 1
        abs_exponent = abs(exponent)
        while abs_exponent != 0:
            res *= base
            abs_exponent -= 1
        if exponent >= 0:
            return res
        else:
            return 1 / res
            