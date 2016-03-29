# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []

        result = []
        path = []

        def dfs(node):
            path.append(str(node.val))

            if not node.left and not node.right:
                result.append("->".join(path))
                path.pop()
                return

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            path.pop()

        dfs(root)

        return result

test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(test.binaryTreePaths(root))




