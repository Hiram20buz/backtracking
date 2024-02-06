class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def permutaciones(s=[]):
            if len(s) == len(nums):  # Base case: If the length of s equals the length of nums, append a copy of s to l
                l.append(s.copy())  # Append a copy of s to l
                return

            for c in nums:
                if c not in s:  # Ensure we are not using the same element more than once
                    s.append(c)
                    permutaciones(s)
                    s.pop()  # Backtrack by removing the last element appended to s

        l = []
        permutaciones()
        return l


print(Solution().permute([1,2,3]))