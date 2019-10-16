#Given a binary tree, return the postorder traversal of its nodes' values.
#
#Example:
#
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
#Output: [3,2,1]
#Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return
        
        stack = []
        stack2 = []
        result = []
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            stack2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        while stack2:
            node = stack2.pop()
            result.append(node.val)

        return result