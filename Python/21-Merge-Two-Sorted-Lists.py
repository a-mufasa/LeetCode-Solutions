class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        merged = None
        if (list1.val < list2.val):
            merged = list1
            merged.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged = list2
            merged.next = self.mergeTwoLists(list1, list2.next)
        return merged
        