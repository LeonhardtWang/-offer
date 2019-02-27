# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:return False
        if len(sequence) <= 2:return True
        
        ver_left = True
        for i, v in enumerate(sequence[:-1]):
            if ver_left:
                if v >= sequence[-1]:
                    ver_left = False
                    sli_i = i
            else:
                if v <= sequence[-1]:
                    return False
        if ver_left:
            return self.VerifySquenceOfBST(sequence[:-1])
        elif sli_i == 0:
            return self.VerifySquenceOfBST(sequence[sli_i:-1])
        else:
            return self.VerifySquenceOfBST(sequence[:sli_i]) & self.VerifySquenceOfBST(sequence[sli_i:-1])
            