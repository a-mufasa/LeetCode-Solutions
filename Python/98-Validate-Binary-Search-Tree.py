class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrderCheck(node, min_val, max_val):
            if node is None:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return inOrderCheck(node.left, min_val, node.val) and inOrderCheck(node.right, node.val, max_val)

        return inOrderCheck(root, float('-inf'), float('inf'))
        