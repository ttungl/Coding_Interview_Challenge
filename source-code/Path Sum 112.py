# 112. Path Sum


# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # sol 1:
        # DFS
        # runtime: 59ms
        def dfs(root, cnt, res):
            if not root.left and not root.right:
                if cnt == sum:
                    res.append(True)
            if root.left: 
                dfs(root.left, cnt+root.left.val, res)
            if root.right: 
                dfs(root.right, cnt+root.right.val, res)

        if not root:
            return False
        cnt, res = 0, []
        dfs(root, root.val, res)
        return any(res)
        
        # sol 2:
        # use stack
        # runtime: 78ms
        if not root:
            return False

        stack = [(root, root.val)]
        
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                if sum == value:
                    return True
            if node.left:
                stack.append((node.left, value + node.left.val))
            if node.right:
                stack.append((node.right, value + node.right.val))
        return False
        
        

