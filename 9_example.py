class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        out = []

        def backtrack(start, seq):
            if len(seq) == k:
                out.append(seq[:])
                return

            for i in range(start, n + 1):
                seq.append(i)
                backtrack(i + 1, seq)
                seq.pop()

        backtrack(1, [])
        return out

print(Solution().combine(4, 2))