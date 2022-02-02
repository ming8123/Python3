
def sortColors(self, nums: List[int]) -> None:
    """
    Two pointers
    """
    inicio = 0 
    final = len(nums)-1
    i = 0
    while i <= final:
        if nums[i] == 0:
            nums[i],nums[inicio] = nums[inicio],nums[i]
            inicio += 1
            i += 1
        elif nums[i] == 2:
            nums[i],nums[final] = nums[final],nums[i]
            final -= 1
        else:
            i += 1
            
            


