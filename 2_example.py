'''
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:      
        def backtrack(path = [], sum = 0):
            #print(self.sum)
            #print(path)
            #print(sum(path))
            
            if sum > target:
                return

            if sum == target:
                    combinations.append(path[:])
                    return
            
            for i in range(len(candidates)):    
                sum = sum + candidates[i]
                path.append(candidates[i])
                backtrack(path, sum)
                sum = sum - candidates[i]
                path.pop()


        combinations = []
        backtrack()
        #return combinations
        
        for lst in combinations:
            lst.sort()
            #print(lst)
        return [list(tpl) for tpl in set(tuple(lst) for lst in combinations)]


a = Solution().combinationSum([2,3,5], 8)
print(a)
'''
for lst in a:
    lst.sort()
    print(lst)
'''
#unique_lists = set(tuple(lst) for lst in a)
#print(unique_lists)

#unique_lists = [list(tpl) for tpl in set(tuple(lst) for lst in a)]
#print(unique_lists)