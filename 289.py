class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                count = 0

                for rd, cd in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nr = i + rd
                    nc = j + cd
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and (board[nr][nc] == 1 or board[nr][nc] == 2):
                        count += 1

                if board[i][j] and (count < 2 or count > 3):
                    board[i][j] = 2
                elif not board[i][j] and count == 3:
                    board[i][j] = 3


        for i in range(0, m):
            for j in range(0, n):
                board[i][j] = board[i][j] % 2
