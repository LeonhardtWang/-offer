# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            sum_ = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum_ & 0xffffffff
            num2 = carry
        return num1 if num1 >> 31 == 0 else num1 - 0xffffffff - 1



if __name__ == "__main__":
    print(Solution().Add(11,34))