from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numPad = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        res, sol = [], []
        n = len(digits)
        letters = [numPad[digit] for digit in digits]

        def backtrack(digitInd: int, charInd: int) -> None:
            if digitInd == n:
                res.append(''.join(sol))
                return
            
            if charInd >= len(letters[digitInd]):
                return
            
            sol.append(letters[digitInd][charInd])
            backtrack(digitInd+1, charInd)
            sol.pop()
            backtrack(digitInd, charInd+1)
            
        backtrack(0,0)

        return res

s = Solution()
s.letterCombinations('23')