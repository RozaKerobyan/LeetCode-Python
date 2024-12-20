class Solution(object):
    def reverseOddLevels(self, root):
        def DFS(child_left, child_right, level):
            if not child_left or not child_right:
                return
            if level % 2 == 0:
                child_left.val, child_right.val = child_right.val, child_left.val
            DFS(child_left.left, child_right.right, level + 1)
            DFS(child_left.right, child_right.left, level + 1)
        DFS(root.left, root.right, 0)
        return root
        