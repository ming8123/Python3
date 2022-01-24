def longestOnes(nums: List[int], k: int) -> int:
    '''
    sliding windows este ejercicio la idea es  usar sliding windows
    pero esta vez no hace falta usar hash map para guardar valor 
    pq solo hay 1 y 0 asique la idea es minimizar la ventana y guarda la 
    ventana mas grande 

    '''
    start = 0 
    max_num  = 0
    repetido = 0 
    
    for n in range(len(nums)):
        if nums[n] == 0:
            repetido += 1
        while repetido > k :               
            if nums[start] == 0:
                repetido -= 1 
            start += 1    
        max_num = max(max_num, n-start+1)
    return max_num