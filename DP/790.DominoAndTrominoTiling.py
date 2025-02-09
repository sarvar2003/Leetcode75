class Solution:
    def numTilings(self, n: int) -> int:
        full = {0: 1, 1: 1}
        topMissing = {1: 0}
        bottomMissing = {1: 0}

        for i in range(2, n+1):
            full[i] = full[i-1] + full[i-2] + topMissing[i-1] +  bottomMissing[i-1]
            topMissing[i] = full[i-2] + bottomMissing[i-1]
            bottomMissing[i] = full[i-2] + topMissing[i-1]
        
        return full[n] % (10 ** 9 + 7)

# Time: O(n)
# Space: O(n)
