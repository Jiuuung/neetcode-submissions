# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """거꾸로된 linked 리스트를 하나 만들기( tail 하나 지정하고 그걸 next로 계속 지정하는 방식)
        이후 한번씩 번갈아가면서 리스트 넣기."""
        slow, fast = head, head.next
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        second= slow.next
        slow.next= None
        prev= None
        while second:
            tmp = second.next
            second.next= prev
            prev= second
            second= tmp
        second= prev

        first= head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


