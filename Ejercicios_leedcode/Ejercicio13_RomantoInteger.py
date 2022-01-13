def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0

        for i in range(len(s)):
            if i > 0 and romanos[s[i]] > romanos[s[i - 1]]:
                entero += romanos[s[i]] - 2 * romanos[s[i - 1]]
            else:
                entero += romanos[s[i]]

        return entero
