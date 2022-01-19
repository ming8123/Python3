import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
   

        """
        sliding windows
        """
        output=math.inf#declaramo una variable que es inifitamente mayor
        cur_sum = 0 
        start = 0
        cur_len = 0
        
        for end in range(len(nums)):
            cur_sum += nums[end]
            cur_len += 1
            while cur_sum >= target:
                output = min(output,cur_len)
                cur_len -= 1 
                cur_sum -= nums[start]
                start += 1
        if output == math.inf:output =0

        return output        
                