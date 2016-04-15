import heapq
import copy

class Solution(object):
    def getBarberNum(self, B, N, M):
        if B >= N:
            return N

        allSame = True
        count = 0
        commonMultiple = 1

        for i in range(len(M)):
            if allSame and M[i] != M[0]:
                allSame = False
            commonMultiple *= M[i]

        if allSame:
            return B if N % B == 0 else N % B

        for i in range(len(M)):
            count += commonMultiple / M[i]

        if N % count != 0:
            count = int(N % count)

        if count < B:
            return count
        else:
            count -= B

        heap = copy.deepcopy(M)

        for i in range(len(heap)):
            heap[i] = (M[i], i + 1)

        heapq.heapify(heap)

        while True:
            mi, i = heapq.heappop(heap)
            count -= 1

            if count == 0:
                return i
            else:
                heapq.heappush(heap, ((mi + M[i - 1]), i))


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    (B, N) = tuple(map(int, input().split(" ")))
    M = [int(mi) for mi in input().split(" ")]
    print("Case #{}: {}".format(i, test.getBarberNum(B, N, M)))
    # check out .format's specification for more formatting options
