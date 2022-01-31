import math

def threeSumClosest(self, nums: List[int], target: int) -> int:
    '''
    Two points
    '''
    length = len(nums)
    minimo = math.inf
    nums.sort()
    for i in range(length-2):
        inicio = i + 1
        final = length - 1
        
        while inicio < final:
            total = nums[i]+nums[inicio]+nums[final]
            if abs(target-total) < abs(minimo):
                minimo = target - total               
                            
            if minimo == 0:
                return target
            if total < target:
                inicio += 1 
            else:
                final -= 1
    return target - minimo
