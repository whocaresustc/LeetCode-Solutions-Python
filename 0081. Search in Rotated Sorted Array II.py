# two pointers
# be careful with duplicates on the two edges, remove them first
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        # deal with the unwanted duplicates in the edges of array
        while left < right and nums[left] == nums[right]:
            left += 1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:  # mid in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
    
        
                    
