# method 2: same idea as dp, but use bits to represent dp[]
# space O(sum), time O(sum^n)
# iterate nums one by one, and add it into the previous sums array
class Solution1(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total%2 == 1:
            return False
        
        bits = 1
        for num in nums:
            bits |= bits << num
        target = total//2
        return bits & (1 << target)

# method 1, use dynamic programming, add element one by one  
# time O(sum*n), n=len(nums), space O(sum)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        total = sum(nums)
        if total %2 == 1:
            return False
        
        target = total//2
        dp = [False]*(target + 1)
        dp[0] = True
        for num in nums:
            for x in range(target-num, -1, -1):
                if dp[x]:
                    dp[x+num] = True
        return dp[target]

# method 3: combinations, try every one, time O(2^n), TLE


"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
