#tionforsingly-linkedlist.
classListNode(object):
    def__init__(self,x):
        self.val=x
     self.next=None

classSolution(object):
    defremoveElements(self,head,val):
    if  head!=None and head.val == val
        head = removeElements(head.next,val)
    else:
        removeElements(head.next,val)
    return  head
"""
:typehead:ListNode
:typeval:int
:rtype:ListNode
"""

