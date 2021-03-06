# sign, and integer overflow
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # check input
        if not str:
            return 0
        
        # strip " "
        for i in range(len(str)):
            if str[i] != ' ':
                start = i
                break  # easy to forget !!!
        else: # only has space
            return 0
        
        # check the sign, and update start
        sign = 1
        if "+" == str[start]:
            start += 1
        elif "-" == str[start]:
            sign = -1
            start += 1
        
        # get the number and check overflow
        res = 0
        i = start
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        while (i < len(str)) and str[i].isdigit():
            if res > INT_MAX//10 or (res == INT_MAX//10 and str[i] > '7'):
                return INT_MAX if sign > 0 else INT_MIN  # typo: sign>1
            else:
                res = res*10 + int(str[i])
            i += 1
        
        return res*sign


"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
             
"""

if __name__ == "__main__":
    print(Solution().myAtoi("+120.3abc"))
    
    