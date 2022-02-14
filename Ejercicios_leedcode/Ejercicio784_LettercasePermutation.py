class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutation = []
        permutation.append(s)
        '''
        subset
        '''
        for x in range(len(s)):
            if s[x].isalpha():
                for y in range(len(permutation)):
                    chars = list(permutation[y])
                    chars[x] = chars[x].swapcase()
                    permutation.append("".join(chars))
            else:
                continue
        return permutation