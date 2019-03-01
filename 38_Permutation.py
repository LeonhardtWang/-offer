# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if len(ss) == 0:
            return res
        if len(ss) == 1:
            res.append(ss)
            return res
        s_help = []
        for i, s in enumerate(ss):
            s_res = []
            if s not in s_help:
                s_help.append(s)
                s_remain = ss[:i] + ss[i+1:]
                s_remain_res = self.Permutation(s_remain)
                for i in s_remain_res:
                    s_res.append(s + i)
                res.extend(s_res)
        return res
                    