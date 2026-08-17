class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(1, len(s)):
            diff = ord(s[i])- ord(s[i-1])
            if diff <0:
                diff = -diff
            total += diff
        
        return total