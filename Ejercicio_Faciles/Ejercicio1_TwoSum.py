def twoSum(nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for posi,i in enumerate(nums):           
            for posi1 in range(posi + 1, len(nums)):
                if nums[posi1] == target - nums[posi]:
                     return([posi,posi1])              

nums=[1,2,3,4,4,4] 
target=8
print(twoSum(nums,target))