def minWindow(self, s: str, t: str) -> str:
    '''
    sliding windows este ejercicio lo que hace es que vas minimizando la ventado y 
    gurdando el rango mas pequeño de la ventana y guardado en una variable inicio
    '''
    lookup = {}
    start = 0 
    minimo = len(s)+1
    cont = 0
    inicio = 0
    for item in t:
        lookup[item] = lookup.get(item,0)+1
    for end in range(len(s)):
        if s[end] in lookup:
            lookup[s[end]] -= 1
            if lookup[s[end]] >= 0:
                cont += 1
        while cont == len(t):
            if minimo > end-start+1:   
                minimo = end -start+1
                inicio = start                
            if s[start] in lookup:                    
                if lookup[s[start]] == 0:
                    cont -= 1
                lookup[s[start]] += 1    
            start += 1

    if minimo >= len(s)+1:
        return ""
    return s[inicio:inicio+minimo]