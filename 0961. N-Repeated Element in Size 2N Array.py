# 1. majority voting will fail
# a straightforward method is to use hashmap or set, time/space O(n)

# this method use the fact that we have N elements appearing only once
# and one element appearing N times

# time O(n), space O(1)
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                return A[i]
        
        if A[0] == A[2] or A[0] == A[3]:
            return A[0]
        else:
            return A[1]




"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
