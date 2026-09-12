# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, 1)])
        last_index = 0
        count = 0

        while queue:
            node, index = queue.popleft()

            if node is None:
                continue

            count += 1
            last_index = index

            queue.append((node.left, 2 * index))
            queue.append((node.right, 2 * index + 1))

        return last_index == count