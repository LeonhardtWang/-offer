# -*- coding:utf-8 -*-
from collections import OrderedDict

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        chr_count_dic = OrderedDict()
        for i, char in enumerate(s):
            if char in chr_count_dic:
                chr_count_dic[char][1] += 1
            else:
                chr_count_dic[char] = [i, 1]
        for k, v in chr_count_dic.items():
            if v[1] == 1:
                return v[0]
        return -1
                

if __name__ == "__main__":
    print(Solution().FirstNotRepeatingChar('google'))