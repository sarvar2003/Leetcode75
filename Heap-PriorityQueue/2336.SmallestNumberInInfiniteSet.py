class SmallestInfiniteSet:

    def __init__(self):
        self.popped = set()
        self.smallest = 1


    def popSmallest(self) -> int:
        smallest = self.smallest
        self.popped.add(smallest)

        self.smallest += 1
        while self.smallest in self.popped:
            self.smallest += 1

        return smallest

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)
        
        self.smallest = min(num, self.smallest) 

# Time: O(n)
# Space: O(n)
# n - number of popped elements