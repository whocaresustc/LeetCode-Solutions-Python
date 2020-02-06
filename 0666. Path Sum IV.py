# time, space O(n)
# bottom up approach
# the child for index i is 2*i and 2*i-1

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        d = {}
        for i in range(len(nums)-1, -1, -1):
            D, P, V = nums[i]//100, (nums[i]//10)%10, nums[i]%10
            cnt = d.get((D+1, 2*P-1), 0) + d.get((D+1, 2*P), 0)
            if cnt == 0: 
                cnt = 1
            d[(D, P)] = cnt
            res += V*cnt
        return res



"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
 

Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 

Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
"""
