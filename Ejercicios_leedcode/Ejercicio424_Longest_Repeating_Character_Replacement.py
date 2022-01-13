def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = {}
        start = 0
        max_rep = 0
        max_len = 0
        
        for end in range(len(s)):
            dic[s[end]]  = dic.get(s[end],0)+1
            max_rep = max(max_rep,dic[s[end]])#hasta aqui buscamos el elmento mas repetido
            if (end - start+1 - max_rep) > k:#solo usamos el elemento mas repetido para una referencia
                dic[s[start]] -= 1
                start += 1
            max_len =max(max_len,end-start+1)
        return max_len 
        