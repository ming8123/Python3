class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        subset.append([])
        end_subset=0
        for x in range(len(nums)):
            start_subset=0
            if x > 0 and nums[x]==nums[x-1]:
                start_subset = end_subset+1
            end_subset = len(subset)-1            
            for y in range(start_subset,end_subset+1):
                curr_subset = list(subset[y])
                curr_subset.append(nums[x])
                subset.append(curr_subset)
        return subset