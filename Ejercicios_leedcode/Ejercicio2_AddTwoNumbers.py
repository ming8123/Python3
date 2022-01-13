# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()#creamos un dummy para guardar listnode
        head = dummy#creamos un head para puntero y asi dummy ya no hace falta que se mueva
        c = 0 #para guardar 1 de avance
        while l1 and l2:#mientra l1 y l2 no este vacio
            head.next = ListNode((l1.val + l2.val + c) % 10)#siquiente puntero(apartir de -1) 
            c = ((l1.val + l2.val + c) // 10)
            l1 = l1.next#que avance el l1
            l2 = l2.next#que avance el l2
            head = head.next#ahora guardamos el head para que el puntero pueda avanzar
        while l1:#en caso de que el l1 sea mayor que l2
            head.next = ListNode((l1.val + c) % 10)
            c = ((l1.val + c) // 10)
            l1 = l1.next
            head = head.next
        while l2:#en caso de que l2 sea mayor que l1
            head.next = ListNode((l2.val + c) % 10)
            c = ((l2.val + c) // 10)
            l2 = l2.next
            head = head.next
            
        if c == 1:#en caso de que sobra un 1
            head.next = ListNode(c)
            
        return dummy.next        