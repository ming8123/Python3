def findAnagrams(s2: str, s1: str) -> List[int]:
    '''
    este ejercicio se usa sliding windows y es casi lo mismo que el ejercicio 567
    '''
    start = 0 
    lookup = {}
    cont = 0 
    resu = []
    for item in s1:
        lookup[item] = lookup.get(item,0)+1
    for end in range(len(s2)):
        if s2[end] in lookup:
            lookup[s2[end]] -= 1
            if lookup[s2[end]] == 0:
                cont += 1 
        if cont == len(lookup):
            resu.append(start)
        if end - start >= len(s1)-1:
            if s2[start] in lookup:                    
                if lookup[s2[start]] == 0:
                    cont -= 1
                lookup[s2[start]]+= 1    
            start += 1              
    return resu
