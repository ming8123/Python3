   def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        start = 0 #para poder recordar cual es el ultimo elemnto repetido 
        max_len = 0 
        dic = {}
        
        for end in range(len(s)):                      
            if s[end] in dic:#comprobar si el elemento esta en diccionario
                start=max(start,dic[s[end]]+1) 
                '''
                indico donde acaba el mayor posicion del elemento repetido 
                ejemplo si es abab la posicion de acacba es 0+1 empieza contar desde b
                uso el max para estos caso abba cuando esta haciendo el for 
                va llegar el segundo a y te va dar el resultado 0+1 y eso no es correcto
                porque el b esta en una posicion mayor 1+1
                
                '''           
            dic[s[end]] = end#guardo el nuevo elemento  o corrijo el elemento a nuevo posicion
            max_len=max(max_len,(end-start+1))    #por ultimo devuelvo el max +1 por que empieza la posicion0
        return max_len