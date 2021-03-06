# 263. Ugly Number
# ttungl@gmail.com
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # sol 1: positive number and contain primes.
        # runtime: 35 ms
        p = [2, 3, 5]
        for i in p:
            while num > 0 and num % i==0: 
                num /= i
        return num==1
        