# use two heaps: time O(n*log(k)), space O(k)
# ref: https://leetcode.com/problems/sliding-window-median/
# discuss/262689/Python-Small-and-Large-Heaps
import heapq
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        small = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(small)
        large = []
        for _ in range((k+1)//2):  # make len(large) >= len(small)
            self.move(small, large)
        
        res = [self.getMedian(small, large, k)]
        for i, num in enumerate(nums[k:]):
            if num < large[0][0]:  # the equal sign here is not import
                heapq.heappush(small, (-num, i+k))
                if nums[i] >= large[0][0]:  # but we must have equal sign for this if
                    self.move(small, large)
            else:
                heapq.heappush(large, (num, i+k))
                if nums[i] <= large[0][0]:  # mistake: if nums[i] <= large[0][0]
                    self.move(large, small)
            # only clear the value in the heap top
            # the number of values in the window are 
            # equally distributed between the two heaps
            # but the values outside the window might still exist in the window
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            if len(small) > 3*k:
                self.clean(small, i)  # amortized time for each i is O(1)
            if len(large) > 3*k:
                self.clean(large, i)
            res.append(self.getMedian(small, large, k))
        
        return res
    
    def clean(self, heap, i):
        # remove all data in the heap that are older than i
        # prevent the heap to become too big
        heap = [(num, j) for num, j in heap if j > i]
        heapq.heapify(heap)
        return heap
    
    
    def move(self, heap1, heap2):
        # pop one element out from heap1, and push it into heap2
        num, i = heapq.heappop(heap1)
        heapq.heappush(heap2, (-num, i))
    
    
    def getMedian(self, small, large, k):
        if k%2 == 0:
            return (-small[0][0] + large[0][0])/2.0
        else:
            return large[0][0]
    
    
    
