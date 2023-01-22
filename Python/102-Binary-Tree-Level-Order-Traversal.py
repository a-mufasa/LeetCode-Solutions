class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def addLevel(node, level, arr):
            if node is None:
                return
            
            if len(arr) < level+1:
                arr.append([])
            
            arr[level].append(node.val)
            addLevel(node.left, level+1, arr)
            addLevel(node.right, level+1, arr)
        
        result = []
        addLevel(root, 0, result)
        return result
            