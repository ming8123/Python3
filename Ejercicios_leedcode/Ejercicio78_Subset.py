class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
       '''
       Ejercicio de tipo subsets
       '''
       
       
        subset = []
        subset.append([])
        
        for x in nums:
            for y in range(len(subset)):
                copy_subset = list(subset[y])
                copy_subset.append(x)
                subset.append(copy_subset)
        return subset