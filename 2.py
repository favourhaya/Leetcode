# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 =l2
        
        addon = 0

        curr1 = head1
        curr2 = head2
        while curr1 !=None and curr2 !=None:
            if curr1 and curr2:  
                if curr1.val + curr2.val + addon > 9:
                    tmp = addon
                    tmp2 = curr1.val
                    addon = (curr1.val + curr2.val+tmp) //10
                    curr1.val = (curr1.val + curr2.val +tmp) % 10
                    curr2.val = (tmp2 + curr2.val +tmp) % 10
  
                else:
                    tmp = curr1.val
                    curr1.val += (curr2.val + addon)
                    curr2.val += (tmp+ addon)
                    addon =0
            

            if curr1:
                last1 =curr1
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next



        if not curr1 and not curr2:
            if addon:
                last1.next = ListNode(addon)
            return l1
        
        if curr1 != None:
            while curr1 != None:
                if curr1.val + addon > 9:
                    tmp = addon
                    addon = (curr1.val+tmp) //10
                    curr1.val = (curr1.val + tmp) % 10
                else:
                    curr1.val +=  addon
                    addon =0
                last = curr1
                    
                curr1 = curr1.next
               
            if addon:
                last.next = ListNode(addon)
            return l1
            
        if curr2 != None:
            while curr2 != None:
                if curr2.val + addon > 9:
                    tmp = addon
                    addon = (curr2.val+tmp) //10
                    curr2.val = (curr2.val + tmp) % 10
                else:
                    curr2.val +=  addon
                    addon =0
                last = curr2 
                curr2 = curr2.next
            if addon:
                last.next = ListNode(addon)
        
        return l2
        
           
                


        