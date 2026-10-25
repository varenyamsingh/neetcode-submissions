# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root, subRoot):
        
        def isSameTree(p, q):
            # Both trees are empty
            if not p and not q:
                return True

            # Only one tree is empty
            if not p or not q:
                return False

            # Values must match
            if p.val != q.val:
                return False

            # Both left and right sides must match
            return (
                isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )

        # Search the big tree
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
