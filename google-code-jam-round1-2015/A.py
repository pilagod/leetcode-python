class Solution(object):
    def minimumMushroom(self, intervals, mushroomNums):
        strategy1 = 0
        strategy2 = 0
        eatingRate = 0
        intervalDiff = 0

        for i in range(intervals - 1):
            intervalDiff = mushroomNums[i] - mushroomNums[i + 1]
            if intervalDiff > 0:
                strategy1 += intervalDiff
            if intervalDiff > eatingRate:
                eatingRate = intervalDiff

        for i in range(intervals - 1):
            intervalDiff = mushroomNums[i] - eatingRate
            if intervalDiff < 0:
                strategy2 += mushroomNums[i]
            else:
                strategy2 += eatingRate

        return (strategy1, strategy2)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    intervals = int(input())
    mushroomNums = [int(num) for num in input().split(" ")]
    (strategy1, strategy2) = test.minimumMushroom(intervals, mushroomNums)
    print("Case #{}: {} {}".format(i, strategy1, strategy2))
    # check out .format's specification for more formatting options
