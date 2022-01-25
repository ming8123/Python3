def checkInclusion(self, s1: str, s2: str) -> bool:
    '''
    sliding windows este ejercicio se usa hash map (dicc) para acordar los elementos que esta en 
    s2 y poder gestionar lo que ha utilizado y lo que no esta junto con la ventana 

    '''
    start = 0 
    lookup = {}
    cont = 0 
    for item in s1:
        lookup[item] = lookup.get(item,0)+1#guardamos todo lo que hay en s2 en dicc
    for end in range(len(s2)):
        #primero intentamos poner una condicion para sacar el resultado 
        if s2[end] in lookup:#mira si el elemento  si esta en lookup 
            lookup[s2[end]] -= 1 #si lo esta lo quitas uno 
            if lookup[s2[end]] == 0:
                cont += 1 #sumamos el contador para condicion del return
        if cont == len(lookup):#esta es la condicion del resultado aqui hay que tener cuidado lo que estas comparando es len de hash map y no de s2
            return True
        if end - start >= len(s1)-1:#"digamos esto es la excepcion del resultado"
            if s2[start] in lookup: #quitamos si start se mueve a una posicion que tenga elem que esta s1                   
                if lookup[s2[start]] == 0:
                    cont -= 1
                lookup[s2[start]]+= 1    
            start += 1              
    return False