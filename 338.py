class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # if num == 0:
        #     return [0]
        #
        # result = [0, 1]
        # nextPowerOfTwo = 2
        #
        # for i in range(2, num + 1):
        #     if (i == nextPowerOfTwo):
        #         prePowerOfTwo = i
        #         nextPowerOfTwo = i * 2
        #         result.append(1)
        #     else:
        #         result.append(result[i - prePowerOfTwo] + 1)

        result = [0] * (num + 1)

        for i in range(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result

test = Solution()
print(test.countBits(0))
print(test.countBits(1))
print(test.countBits(5))
print(test.countBits(10))