# combination sum
# DFS recursion
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 1:
            return []
        res = []
        self.dfs([], n, res)
        return res
    
    def dfs(self, path, n, res):
        if path:
            if n < path[-1]:
                return
            res.append(path+[n])
        start = 2 if not path else path[-1]
        for num in range(start, int(n**0.5)+1):   # make sure path[-1] <= num <= next_num
            if n%num == 0:
                path.append(num)
                self.dfs(path, n//num, res)
                path.pop()



"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible 
combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""
