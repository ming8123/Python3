
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:        
    '''
    Two pointer con dos for
    '''
    res = []
    length = len(nums)
    nums.sort()
    
    for i in range(len(nums)-3):
        if i > 0 and nums[i]==nums[i-1]:
            continue 
        for j in range(i+1,length-2):
            if j > i+1 and nums[j]==nums[j-1]:
                continue 
            inicio = j + 1
            final = length - 1

            while final > inicio:
                total = nums[i]+nums[j]+nums[inicio]+nums[final]
                if total > target:
                    final -= 1                    
                elif total < target:
                    inicio += 1
                else:
                    res.append([nums[i],nums[j],nums[inicio],nums[final]])

                    while inicio<final and nums[inicio] == nums[inicio+1]:
                        inicio += 1
                    while inicio<final and nums[final] == nums[final-1]:
                        final -= 1

                    inicio+=1
                    final-=1
    if len(res)==0:
        return []
    return res
