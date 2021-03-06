"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
__author__ = 'Xiaoli'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.current = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current or self.stack

    def next(self):
        """
        :rtype: int
        :return: the next smallest number
        """
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        next_node = self.stack.pop()
        self.current = next_node.right
        return next_node.val


