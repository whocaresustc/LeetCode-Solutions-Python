# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# expected number of call for rand7 for each rand10() is 2/(40/49)
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        num = 40
        while num >= 40:
            num = 7*(rand7()-1) + (rand7()-1)
        return num%10 + 1
    
# a better solution by Lee215
# ref: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C%2B%2BJavaPython-1.183-Call-of-rand7-Per-rand10

"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
"""
