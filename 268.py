class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        return length * (length + 1) / 2 - sum(nums)

test = Solution()
print(test.missingNumber([0, 1, 3]))
print(test.missingNumber([0]))

