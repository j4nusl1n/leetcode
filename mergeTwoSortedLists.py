# https://leetcode.com/problems/merge-two-sorted-lists
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        head = cur = ListNode()
        while list1 and list2:
            # print(cur1, cur2)
            if list2.val >= list1.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        cur.next = list1 or list2
        return head.next
