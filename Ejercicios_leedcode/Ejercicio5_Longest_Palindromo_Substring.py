 def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        longmax=""
        
        def palindromo(s,l,r):#creamos una funcion nuevo para no estar repitiendo el codigo
            '''
            lo que hace este codigo principalmente es coger una letra cadena
            y comprobar si es palindromo
            '''
            res = ""
            while l >= 0 and r < len(s) and s[l]==s[r]:
                '''
                mientra que la indicador de posicion de izquierda no se menor que 0
                y que el indicador de derecha no supera el longitud de la cadena 
                y que sea iguale 
                '''
                res = s[l:r+1]
                l -= 1#movemos a una posicion a la izquierda
                r += 1#movemos a una posicion a la derecha
            return res
        for i in range(len(s)):#recorremos la cadena 
            word1=palindromo(s,i,i)#utilizmos la funcion que hemos creado para comprobar (aba,ccc)ejemplo
            word2=palindromo(s,i,i+1)#este es para comprobar los que son tipo(aa,aabb)
            if len(word1) > len(longmax):#solo queremos el palindromo con mayor longitud
                longmax=word1
            if len(word2) > len(longmax):
                longmax=word2
        return longmax         
   