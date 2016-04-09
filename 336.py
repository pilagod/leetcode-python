class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dict = {}
        result = []

        for i in range(len(words)):
            dict[words[i]] = i

        for i in range(len(words)):
            for j in range(len(words[i])+1):
                prefix = words[i][:j]
                suffix = words[i][j:]

                reversedPrefix = prefix[::-1]
                reversedSuffix = suffix[::-1]

                if j != 0 and prefix == reversedPrefix and reversedSuffix in dict and dict[reversedSuffix] != i:
                    result.append([dict[reversedSuffix], i])

                if suffix == reversedSuffix and reversedPrefix in dict and dict[reversedPrefix] != i:
                    result.append([i, dict[reversedPrefix]])

        return result

test = Solution()
print(test.palindromePairs(["bat", "tab", "cat"]))