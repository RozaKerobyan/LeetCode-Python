class Solution(object):
    def canChange(self, start, target):
        if start == target:
            return True
        
        left = 0
        right = 0
        for i, j in zip(start, target):
            if i == 'R':
                if left > 0:
                    return False
                right += 1
            if j == 'L':
                if right > 0:
                    return False
                left += 1
            if j == 'R':
                if right == 0:
                    return False
                right -= 1
            if i == 'L':
                if left == 0:
                    return False
                left -= 1
        return right == 0 and left == 0
        