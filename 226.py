# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if not root.left and not root.right:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root

test = Solution()

# Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

result = test.invertTree(root)

print(result.val, result.left.val, result.right.val)

# Case 2
root = TreeNode(1)

result = test.invertTree(root)
print(result.val, result.left.val if result.left else result.left, result.right.val if result.right else result.right)
