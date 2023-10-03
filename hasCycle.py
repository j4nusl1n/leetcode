class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur:
            if cur.val is None:
                return True
            cur.val = None
            cur = cur.next
        return False
