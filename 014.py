class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs)

test = Solution()
print(test.longestCommonPrefix(["abcde", "acdbe", "aaaaa"]))
print(test.longestCommonPrefix(["a"]))