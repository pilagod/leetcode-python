class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''

        while n > 26:
            remains = n % 26

            if remains == 0:
                remains = 26

            n = ( n - remains ) / 26
            result = chr(remains + 64) + result

        return chr(n + 64) + result

