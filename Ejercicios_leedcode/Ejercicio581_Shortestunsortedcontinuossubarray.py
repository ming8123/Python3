
import math
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        Two pointers
        '''
        inicio = 0 
        final = len(nums)-1
        num_max = float('-inf')
        num_min = float('inf')
        
        while inicio < final and nums[inicio]<=nums[inicio+1]:
            inicio += 1
        #edge check
        if inicio == final:
            return 0
           
        while final > inicio and nums[final] >= nums[final-1]:
            final -= 1

        for i in range(inicio,final+1):
            num_max=max(num_max,nums[i])
            num_min=min(num_min,nums[i])
            
        while inicio > 0 and nums[inicio-1] > num_min:
            inicio -= 1
        while final < len(nums)-1 and nums[final+1] < num_max:
            final += 1
        return final-inicio+1