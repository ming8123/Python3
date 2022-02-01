def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    inicio = 0
    count = 0 
    producto = 1
    '''
    two points pero esta vez solo hemos necesitado 2 points
    for final in range(len(nums)): count += fianl-inicio+1
    total las posiblidades que existe para combinar numeros
    '''
    for final in range(len(nums)):
        producto *= nums[final]
        while producto >= k and final >= inicio:
            producto /= nums[inicio]
            inicio += 1
        count += (final-inicio+1)
    return count
