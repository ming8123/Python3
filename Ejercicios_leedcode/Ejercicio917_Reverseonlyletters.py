class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        '''
        Two pointers
        '''
        
        lista_s = list(s)
        left = 0
        right = len(s)-1
        
        while right >left:
            while right > left and not lista_s[right].isalpha():
                right -= 1
            while right > left and not lista_s[left].isalpha():
                left += 1
                
            lista_s[right],lista_s[left] = lista_s[left],lista_s[right]
            
            right -= 1
            left += 1
        return "".join(lista_s)