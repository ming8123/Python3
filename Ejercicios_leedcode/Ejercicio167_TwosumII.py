def twoSum(self, numbers: List[int], target: int) -> List[int]:
    inicio = 0
    final = len(numbers)-1
    '''
    Two points este ejercicio para resolver se usa el metodo de Two points
    '''
    
    
    while final > inicio:
        resultado = numbers[inicio]+numbers[final]
        if resultado == target:
            return[inicio+1,final+1]
        if resultado > target:
            final=final-1
        if resultado < target:
            inicio=inicio +1
    return [-1,-1]        
            