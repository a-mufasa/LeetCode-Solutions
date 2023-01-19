class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        if head.next.next is None:
            return head.next
        
        middle = head

        while head is not None:
            if head.next is None:
                break
            middle = middle.next
            head = head.next.next
        return middle
        