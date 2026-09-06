# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur=head
        while cur!=None:
            length+=1
            cur= cur.next
        cur= head
        if length-n>0:
            for j in range(length-n-1):
                cur=cur.next
            cur.next= cur.next.next
        else:
            return cur.next
        return head