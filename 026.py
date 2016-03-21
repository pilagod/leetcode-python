class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        current = nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] != current:
                if i != length:
                    nums[length] = nums[i]
                current = nums[i]
                length += 1

        nums = nums[:length]
        return length

test = Solution()
print(test.removeDuplicates([1, 2, 2]))