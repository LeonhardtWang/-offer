# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        for num in numbers:
            if num < 0 or num > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication.append(numbers[i])
                    return True
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
        return False


if __name__ == "__main__":
    numbers = [2, 3, 1, 0, 2, 5, 3]
    duplicate = []
    print(Solution().duplicate(numbers, duplicate))
    print(duplicate)