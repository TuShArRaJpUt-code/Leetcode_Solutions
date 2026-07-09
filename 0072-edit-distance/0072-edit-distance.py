class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        return self.solve(word1, word2, n, m, dp)

    def solve(self, word1, word2, i, j, dp):

        if i == 0:
            return j

        if j == 0:
            return i

        if dp[i][j] != -1:
            return dp[i][j]

        if word1[i-1] == word2[j-1]:
            dp[i][j] = self.solve(word1, word2, i-1, j-1, dp)
        else:
            ins = 1 + self.solve(word1, word2, i, j-1, dp)
            dele = 1 + self.solve(word1, word2, i-1, j, dp)
            rep = 1 + self.solve(word1, word2, i-1, j-1, dp)

            dp[i][j] = min(ins, dele, rep)

        return dp[i][j]