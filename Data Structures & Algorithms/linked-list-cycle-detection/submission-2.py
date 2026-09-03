# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #모든 방문을 저장해두고 재방문 확인하기
        visited={head}
        cur=head
        while cur:
            if cur.next in visited:
                return True
            else:
                visited.add(cur)
                cur=cur.next
        return False

        #sol 제시 방법: fast와 slow를 두고 fast는 두칸씩, slow는 한칸씩 이동하면서 언젠가 만나는지 보기
        # 만난다면 cycle이 있는것, fast가 null에 먼저 도달하게 된다면 cycle은 없는것이됨.