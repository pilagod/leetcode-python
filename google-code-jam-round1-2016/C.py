class Solution(object):
    def getMaxCircle(self, num, bffs):

        def makePath(kid):
            firstRound = True
            result = []
            result.append(kid)

            kid = bffs[kid]

            while True:
                # print(result, kid, bffs[kid])
                if bffs[kid] == result[0]:
                    result.append(kid)
                    return (True, result)
                elif bffs[kid] == result[-1]:
                    result.append(kid)
                    return (False, result)
                elif not firstRound and bffs[kid] in result:
                    return (False, [])

                result.append(kid)
                kid = bffs[kid]
                firstRound = False

        def dfs(path):
            result = []

            for i in range(num):
                if i not in path:
                    if path[0] == bffs[i]:
                        result.append(dfs([i] + path))

                    if path[-1] == bffs[i]:
                        result.append(dfs(path + [i]))

            if len(result) == 0:
                return len(path)
            else:
                return max(result)

        result = []
        paths = []
        for i in range(num):
            isCircle, curPath = makePath(i)
            # print(isCircle, curPath)
            if isCircle:
                result.append(len(curPath))
            if not isCircle and len(curPath) > 0:
                paths.append(curPath)

        for i in range(len(paths)):
            result.append(dfs(paths[i]))

        # TODO: dfs

        return max(result)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    num = int(input())
    bffs = [int(bff) - 1 for bff in input().split(' ')]
    print("Case #{}: {}".format(i, test.getMaxCircle(num, bffs)))
    # check out .format's specification for more formatting options
