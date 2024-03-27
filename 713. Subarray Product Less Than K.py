#https://leetcode.com/problems/subarray-product-less-than-k/?envType=daily-question&envId=2024-03-27
#Done by Murshed Jamil Alif
class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        if k <= 1:
            return 0
        
        count = 0
        left = 0
        product = 1
        
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
        
        return count
