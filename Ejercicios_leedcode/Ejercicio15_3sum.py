
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    length = len(nums)
    nums.sort()
    '''
    lo mismo se usa el metodo de two points 
    
    '''
    for i in range(len(nums)-2):
        if i > 0 and nums[i]==nums[i-1]:
            continue 
        inicio = i + 1
        final = length - 1
        
        while final > inicio:
            total = nums[i]+nums[inicio]+nums[final]
            if total > 0:
                final -= 1                    
            elif total < 0:
                inicio += 1
            else:
                res.append([nums[i],nums[inicio],nums[final]])
            
                while inicio<final and nums[inicio] == nums[inicio+1]:
                    inicio += 1
                while inicio<final and nums[final] == nums[final-1]:
                    final -= 1

                inicio+=1
                final-=1
    return res
        