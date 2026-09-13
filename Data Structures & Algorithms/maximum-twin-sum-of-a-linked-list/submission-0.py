# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
            # Find length
        n = 0
        current = head

        while current:
            n += 1
            current = current.next

        # Put first half into stack
        stack = []

        current = head

        for _ in range(n // 2):
            stack.append(current.val)
            current = current.next

        # Process second half
        max_sum = 0

        while current:
            max_sum = max(max_sum, current.val + stack.pop())
            current = current.next

        return max_sum