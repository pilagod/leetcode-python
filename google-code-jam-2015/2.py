class Solution(object):
    def minimumDiningMinute(self, num_diners, dis_pancakes):
        maxNum = max(dis_pancakes)

        if maxNum <= 2:
            return 2

        return 0

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    num_diners = int(input())
    dis_pancakes = [int(num) for num in input().split(' ')]
    print("Case #{}: {}".format(i, test.minimumDiningMinute(num_diners, dis_pancakes)))