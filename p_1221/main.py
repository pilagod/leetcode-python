class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result, r_count, l_count = 0, 0, 0
        for c in s:
            if c == 'L':
                l_count += 1
            if c == 'R':
                r_count += 1
            if r_count == l_count:
                result += 1
                r_count = 0
                l_count = 0
        return result

