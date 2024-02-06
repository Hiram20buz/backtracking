class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def permutaciones(s=[]):
            if len(s) == len(nums):  # Base case: If the length of s equals the length of nums, append a copy of s to l
                #l.append(s.copy())  # Append a copy of s to l
                l.add(tuple(s.copy()))
                return

            for i in range(len(nums)):
                if not used[i]:
                    s.append(nums[i])
                    used[i] = True  # Mark the current element as used
                    permutaciones(s)
                    s.pop()  # Backtrack by removing the last element appended to s
                    used[i] = False  # Unmark the current element after backtracking

        #l = []
        nums.sort()
        l = set()
        used = [False] * len(nums)  # Initialize a boolean array to keep track of used elements
        permutaciones()
        return l
        '''
        unique_elements = []

        for sublist in l:
            if sublist not in unique_elements:
                unique_elements.append(sublist)
        
        return unique_elements
        '''

print(Solution().permuteUnique([1,1,2]))