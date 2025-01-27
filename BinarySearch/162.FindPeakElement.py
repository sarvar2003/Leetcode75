class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            mid = (high + low) // 2

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid -1
        
        return low

# Time: O(log(n))
# Space: O(1)