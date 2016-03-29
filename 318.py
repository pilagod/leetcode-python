class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        A = ord('a')
        bits = [0] * len(words)
        lengths = []
        maxProduct = 0

        for i in range(len(words)):
            lengths.append(len(words[i]))
            for c in words[i]:
                bits[i] |= 1 << (ord(c) - A)

        lengths = [length for length in sorted(enumerate(lengths), key=lambda x: x[1], reverse=True)]

        for i in range(len(words) - 1):
            if lengths[i][1] * lengths[i][1] <= maxProduct:
                break
            for j in range(i + 1, len(words)):
                if (bits[lengths[i][0]] & bits[lengths[j][0]] == 0):
                    maxProduct = max(maxProduct, lengths[i][1] * lengths[j][1])
                    break

        return maxProduct


test = Solution()
print(test.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(test.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(test.maxProduct(["a", "aa", "aaa", "aaaa"]))



