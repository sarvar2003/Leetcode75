class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n+1
        
        while True:
            mid = (high+low)//2
            g = guess(mid) 

            if g == -1:
                high = mid
            elif g == 1:
                low = mid
            else: 
                return mid
            
s = Solution()
s.guessNumber(10)

# Time: O(log(n))
# Space: O(1)