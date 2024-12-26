from collections import deque

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        n = deque()
        n.append(root)
        arr = []
        while n:
            max_value = float('-inf')
            for _ in range(len(n)):
                node = n.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    n.append(node.left)
                if node.right:
                    n.append(node.right)
            arr.append(max_value)
        return arr
        