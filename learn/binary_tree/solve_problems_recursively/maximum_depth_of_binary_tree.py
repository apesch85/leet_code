# Maximum Depth of Binary Tree
# Solution
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest 
# path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.path.append('..')
from binary_tree import BinaryTree

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
        	return 0

        # As we recursively call maxDepth, we are adding 1 + 1n, where n
        # is the number of times either root.left or root.right exists at
        # each recursive call.
        #
        # The max() function then decides which branch is greater, or in
        # other words, which branch has more depth.

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
	
	# Just building the tree pictured above.
	example_tree = BinaryTree(3)
	example_tree.insertLeft(9)
	example_tree.insertRight(7)
	example_tree.insertRight(20)
	new_node = example_tree.getright()
	new_node.insertLeft(15)
	new_node.insertLeft(10)
	
	print Solution().maxDepth(example_tree)

	

main()