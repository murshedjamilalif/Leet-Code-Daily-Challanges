class Solution:
    def maxSubarrayLength(self, nums, k):
        left = 0
        max_length = 0
        freq_map = {}
        
        for right in range(len(nums)):
            # Increment the frequency of the current element
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
            
            # If the frequency exceeds k, start shrinking the window from the left
            while freq_map[nums[right]] > k:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
