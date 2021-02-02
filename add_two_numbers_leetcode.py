# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        node1 = l1
        node2 = l2
        carry = 0
        
        fsum = l1.val + l2.val
        
        if fsum < 10:
            list_sum = ListNode(val=fsum)
            ls_node = list_sum
            carry = 0
        else:
            list_sum = ListNode(val=fsum%10)
            ls_node = list_sum
            carry = 1
            
        node1 = l1.next
        node2 = l2.next
        
        while node1 != None or node2 != None:
            ls_node.next = ListNode()
            ls_node = ls_node.next
            if node1 != None and node2 != None:
                node_sum = node1.val + node2.val + carry
                    
                node1 = node1.next
                node2 = node2.next
                    
            elif node1 == None:
                node_sum = node2.val + carry
                node2 = node2.next
            
            elif node2 == None:
                node_sum = node1.val + carry
                node1 = node1.next
                
            if node_sum < 10:
                ls_node.val = node_sum
                carry = 0
            else:
                ls_node.val = int(node_sum%10)
                carry = 1
        
        if carry != 0:
            ls_node.next = ListNode(val=carry)
            ls_node = ls_node.next
            
        ls_node.next = None
        
        return list_sum