import heapq
import copy
import math
import os

class Solution(object):
    def getBarberNum(self, B, N, M):
        if B >= N:
            return N

        allSame = True

        for i in range(B):
            if allSame and M[i] != M[0]:
                allSame = False
                break

        if allSame:
            return B if N % B == 0 else N % B

        pre = 1
        cur = 1
        curSum = 0

        while curSum < N:
            curSum = 0
            pre = cur
            cur = cur * 2
            for i in range(B):
                curSum += math.floor(cur / M[i]) + 1

        while cur > pre:
            curSum = 0
            middle = math.floor((pre + cur) / 2)

            for i in range(B):
                curSum += math.floor(middle / M[i]) + 1

            if curSum > N:
                cur = middle - 1
            elif curSum < N - B:
                pre = middle + 1
            else:
                break

        # TODO: compare curSum and N
        targetNum = N - curSum

        if targetNum == 0:
            middle -= M[0]
            curSum = 0

            for i in range(B):
                curSum += math.floor(middle / M[i]) + 1

            targetNum = N - curSum

        firstRound = True
        count = 0

        while True:
            curMin = float("inf")

            for i in range(B):
                remaining = middle % M[i]

                if not firstRound and remaining == 0:
                    count += 1
                    if count == targetNum:
                        return i + 1

                if M[i] - remaining < curMin:
                    curMin = M[i] - remaining

            middle += curMin
            firstRound = False

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    (B, N) = tuple(map(int, input().split(" ")))
    M = [int(mi) for mi in input().split(" ")]
    print("Case #{}: {}".format(i, test.getBarberNum(B, N, M)))
    # check out .format's specification for more formatting options
