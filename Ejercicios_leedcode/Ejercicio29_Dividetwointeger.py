 def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        c ,time = 0,0 
        negative = False#lo ideal es que uses -1 y no True y False
        if dividend < 0 or divisor < 0:
            negative = True
            if dividend < 0 and divisor < 0:
                negative = False             
            dividend = abs(dividend)
            divisor = abs(divisor)        
        while dividend >= divisor: 
            temp = dividend - (divisor << time)#super importate aqui<< este se refiere ir a una posicion hacia la izquierda forma binario
            if temp >= 0: #comparamos el variable que hemos creado temporalmente           
                c += (1 << time)
                time += 1#se refiere mas bien la posicion
                dividend = temp#una vez que ha entrado el bucle "correcto" y apodemos modificar el variable original
            else:
                time -= 1#en caso de que supera le bajamos una posicion       
        if negative:           
            c = 0-c       
        '''
        esto de abajo es un limite que ha establecido el enunciado
        '''
        if c > 2**31-1:
            return 2**31-1 
        elif c < -2**31:
            return -2**31 
        else:
            return c