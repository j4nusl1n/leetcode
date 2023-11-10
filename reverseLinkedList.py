# https://leetcode.com/problems/reverse-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.iterative(head)

    def iterative(self, head):
        new_head = None
        while head:
            new_head = ListNode(val=head.val, next=new_head)
            head = head.next

        return new_head

    def recursive(self, node):
        if node is None or node.next is None:
            return node
        n2 = self.recursive(node.next)
        node.next.next = node
        node.next = None
        return n2
