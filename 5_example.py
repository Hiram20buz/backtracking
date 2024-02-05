class Solution:
    def combinationSum2(self, can: list[int], tar: int) -> list[list[int]]:
        can.sort()
        res = set()
        curr = []
        self.solve(can , curr , res , 0 , tar)
        # print(res , can)
        # res = set(res)
        return res

    def solve(self , can:list[int] , curr:list[int] , res:set() , ind:int , tar:int):

        if tar == 0 :
            res.add(tuple(curr))
            return
        if tar < 0 :
            return 
        if ind == len(can):
            return

        n = len(can)

        for i in range(ind , n):
            if i > ind and can[i] == can[i-1] :
                continue
            
            if can[i] > tar :
                break
            
            curr.append(can[i])
            self.solve(can , curr , res , i+1 , tar-can[i])
            curr.pop()

        return 

    