class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def recursiveFunc(node, arr):
            if node is None:
                return
            arr.append(node.val)
            for child in node.children:
                recursiveFunc(child, arr)

        result = []
        recursiveFunc(root, result)
        return result
