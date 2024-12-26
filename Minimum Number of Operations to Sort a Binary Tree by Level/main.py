from collections import deque

class Solution(object):
    def minimumOperations(self, root):
        answer = 0
        n = deque([root])

        while n:
            values = []
            child = list(range(len(n)))
            for _ in (range(len(n))):
                node = n.popleft()
                values.append(node.val)
                if node.left:
                    n.append(node.left)
                if node.right:
                    n.append(node.right)
            
            child.sort(key = lambda i:values[i])

            for i in range(len(child)):
                while child[i] != i:
                    answer += 1
                    child[child[i]], child[i] = child[i], child[child[i]]
        return answer        