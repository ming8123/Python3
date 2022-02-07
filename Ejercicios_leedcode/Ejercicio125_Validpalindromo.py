class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        
        Two pointers
        '''
        if  not s:
            return True
        s = s.lower()
        left = 0
        right = len(s)-1
        
        while right > left:
            while right > left and not s[right].isalnum():
                right -= 1
            while right > left and not s[left].isalnum():
                left += 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True