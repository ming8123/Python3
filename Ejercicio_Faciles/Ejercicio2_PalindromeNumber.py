def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """     
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

print(isPalindrome(121))       