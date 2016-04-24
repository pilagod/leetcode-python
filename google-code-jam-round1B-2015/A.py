class Solution(object):
    def getMinimumCount(self, N):
        # get nums of N's last digit to 1
        lastToOne = int(N[-1]) - 1

        if lastToOne < 0:
            # last digit is 0, minus 9
            # e.g. 100 -> 91
            lastToOne = 9
            N = str(int(N) - 9)
        else:
            N = str(int(N) - lastToOne)

        # create minimum nums table to 10 ** n, n from 0 to 14
        digitsTable = {}
        digitsTable[1] = 1
        digitsTable[10] = 10
        for i in range(2, 15):
            # e.g. 1099 -> 9901 is more efficient than 1009 -> 9001 -> 9901
            bestAddedNums = int('9' * int(i / 2))
            digitsTable[10 ** i] = digitsTable[10 ** (i - 1)] + bestAddedNums + \
                                   (10 ** i - int(str(10 ** (i - 1) + bestAddedNums)[::-1])) + 1

        digits = len(N)
        # e.g. 3 digits minimum number is 10^(3-1)
        digitsMin = (10 ** (digits-1))

        reversedNum = int(N[::-1])
        minCount = reversedNum - digitsMin + lastToOne + (1 if reversedNum != int(N) else 0)

        # traverse all possible, O(len(N))
        for i in range(digits - 2):
            diff = (10 ** (i + 1) * int(N[digits - 1 - i - 1]))
            # e.g.
            #         N: 8156 -> (diff = 5) 8151 -> (diff = 50) 8101 -> (diff = 100) 8001
            # lastToOne:    0 ->               5 ->           50 + 5 ->      100 + 50 + 5
            N = str(int(N) - diff)
            lastToOne += diff

            reversedNum = int(N[::-1])
            temp = reversedNum - digitsMin + lastToOne + (1 if reversedNum != int(N) else 0)

            if temp < minCount:
                minCount = temp

        # print(minCount, digitsMin, lastToOne)
        # print(minCount + digitsTable[digitsMin])

        return minCount + digitsTable[digitsMin]


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    N = input()
    print("Case #{}: {}".format(i, test.getMinimumCount(N)))
    # check out .format's specification for more formatting options
