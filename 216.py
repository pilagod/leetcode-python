class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        if n < k*(k+1)/2:
            return []

        table = [[None]*(n+1) for i in range(k+1)]

        for i in range(1, k+1):
            for j in range(int(i*(i+1)/2), n+1):
                table[i][j] = []
                if i == 1:
                    if j < 10:
                        table[i][j].append([j])
                    continue

                num = 1
                while True:
                    if j-num < 1:
                        break
                    if table[i-1][j-num]:
                        for element in table[i-1][j-num]:
                            if min(element) > num:
                                table[i][j].append([num] + element)
                    num += 1

        return table[k][n]


Instance = Solution()
print(Instance.combinationSum3(8, 36))