class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val

            root.right = self.deleteNode(root.right, root.val)
        
        return root
    
# Time: O(logn)
# Space: O(1)