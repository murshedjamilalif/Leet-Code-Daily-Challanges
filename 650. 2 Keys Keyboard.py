#https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19
#Done by Murshed Jamil Alif
class Solution:
    def minSteps(self, n: int) -> int:
        # Base case: if n is 1, we don't need any operations
        if n == 1:
            return 0
        
        # Initialize the result
        result = 0
        
        # Find the largest factor of n
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                result += i
                n //= i
        
        # If n is still greater than 1, it means n itself is a prime number
        if n > 1:
            result += n
        
        return result
    
