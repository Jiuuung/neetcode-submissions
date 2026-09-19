# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None: return 0
        ret =1
        if root.left==None and root.right==None: return ret
        if root.left !=None:
            ret= 1+self.maxDepth(root.left)
        if root.right !=None:
            ret= max(ret, 1+self.maxDepth(root.right))
        return ret