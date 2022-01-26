
def findSubstring(self, s: str, words: List[str]) -> List[int]:
    '''
    Sliding windows este es uno de los mas dificil he tenido que hacer dos for con diferente 
    window los ejercicios anteriores con un start sustituias el for
    '''
    lookup = {}
    word_len = len(words)
    word_count = len(words[0])
    result = [] 
    for item in words:
        lookup[item] = lookup.get(item,0)+1
    
    for i in range(len(s)-word_len*word_count+1):
        lookup_1 = {}
        for j in range(0,word_len):
            word_index=i+j*word_count
            word = s[word_index:word_index+word_count]
            if word not in lookup:
                break
            lookup_1[word] = lookup_1.get(word,0)+1
            if lookup_1[word] > lookup.get(word,0):
                break
            if j+1 == word_len:
                result.append(i)
    return result
            
        
        
        