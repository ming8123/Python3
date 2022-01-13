def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        parentesis = {")": "(",
                 "}": "{",
                 "]": "["}
        x = []
        if(len(s)%2):
            return False      
        #en caso de que sea impar seguro esta mal por eso devuelve en False
        for c in s:
            if(c in ["(", "{", "["]):
                #comprobamos so esta en los keys del diccionario y lo guardamos
                x.append(c)
            elif((len(x) == 0) or (parentesis[c]!=x.pop())):
                #comprobamos que si al quita con funcion pop(en orden de derecha a izquierda)
                #si esta bien el orden el primer len es para comprobar si existe parentesis o corchetes
                return False
        if (len(x)!= 0):
            #comprobamos del todo si estaba todo correcto si no estuviera en 0 significa que ha quedado algun parentesis iguales por ejemplo "(("

            return False
        
        return True
