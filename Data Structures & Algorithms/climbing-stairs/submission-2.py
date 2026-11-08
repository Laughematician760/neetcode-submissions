class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.helper(n)
    
    def helper(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            result = 1
        if n == 2:
            result = 2
        elif n-2 > 0 and n-1 > 0:
            result = self.helper(n-2) + self.helper(n-1)
        self.memo[n] = result
        return result
        
       
        
        
        
        