# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        return self.matchCore(s, pattern)
    
    def matchCore(self, s, pattern):
        if not s and not pattern:
            return True
        if s and not pattern:
            return False
        if pattern[1:2] == '*':
            if  s and (pattern[0] == '.' or pattern[0] == s[0]):
                return (self.matchCore(s[1:], pattern[2:]) or
                        self.matchCore(s[1:], pattern) or
                        self.matchCore(s, pattern[2:]))
            else:
                return self.matchCore(s, pattern[2:])
        
        if s and (s[0] == pattern[0] or (pattern[0] == '.')):
            return self.matchCore(s[1:], pattern[1:])
        return False

        

if __name__ == "__main__":
    print(Solution().match("",".*"))
    print(Solution().match("bcbbabab",".*a*a"))