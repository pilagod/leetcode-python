class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)

        nums.sort()

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]

            j = i + 1
            k = length - 1

            while (j < k):
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])

                    while(j < k and nums[j] == nums[j + 1]):
                        j += 1

                    while(j < k and nums[k] == nums[k - 1]):
                        k -= 1

                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

        return result

test = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(test.threeSum(nums))
print(test.permuteUnique(nums))


# ver 1
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
#         length = len(nums)
#
#         nums.sort()
#
#         for i in range(length - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for j in range(i + 1, length - 1):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 for k in range(j + 1, length):
#                     if k > j + 1 and nums[k] == nums[k - 1]:
#                         continue
#
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.append([nums[i], nums[j], nums[k]])
#
#         return result