    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for i in range(len(haystack)+1):#he tenido que añadir +1 en rango 
            if (haystack[i:i+l] == needle):#pq si el longitud de haystack es 0 no va recorrer
                return i
        
        return -1