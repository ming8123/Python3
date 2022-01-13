def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0):return ""
        if strs[0]=='':return ''
        #descartamos la opcion de que sea vacio o que la primer elemento sea vacio
        k=0
        #iniciamos una variable para que pueda recorrer el bucle y comprobarlo sin parar
        while(True):
                if(k>=len(strs[0])):return strs[0][:k]
                #retorna si la primera palabra haya acabado
                for c in range(1,len(strs)):
                    if(k>=len(strs[c])):return strs[0][:k]
                    #retorna si cualquier palabra que este ne la lista se haya acabado
                    if(strs[c][k]!=strs[0][k]):return strs[0][:k]
                    #retorna si cualquier letra que no coincida 
                k=k+1