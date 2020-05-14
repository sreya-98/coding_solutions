"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        p = int(pow(num,0.5))
        for i in range(2, p+1):
            if i*i == num:
                return True
        return False
