class Solution(object):
    def minimunInvitedClap(self, s_max, s_n):
        currentInvited = 0
        minInvited = 0

        for i, s in enumerate(s_n):
            s = int(s)

            if i > 0 and s > 0 and currentInvited < i:
                needInvited = i - currentInvited
                minInvited += needInvited
                currentInvited += needInvited

            currentInvited += s

        return minInvited


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
  s_max, s_n = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
  s_max = int(s_max)
  print("Case #{}: {}".format(i, test.minimunInvitedClap(s_max, s_n)))
  # check out .format's specification for more formatting options
