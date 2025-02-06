class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (n)

        def dp(ind: int, money: int, memo: List[int]) -> int:
            if ind >= n:
                return money 
            
            if memo[ind]:
                return memo[ind]
            
            if not nums[ind]:
                memo[ind] = dp(ind+1, money, memo)
            else:
                memo[ind] = max(nums[ind] + dp(ind+2, money, memo), dp(ind+1, money, memo))
            
            money += memo[ind]

            return memo[ind]
        
        return dp(0, 0, memo)

# Time: O(n)
# Space: O(n)