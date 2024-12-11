class Solution(object):
    def maximumLength(self, s):
        count = [[0] * (len(s) + 1) for _ in range(26)]
        max_length = -1 
        i = 0
        while i < len(s):
            curr = s[i]
            j = i
            while i < len(s) and s[i] == curr:
                i += 1
            size = 1
            while j < i:
                char_index = ord(curr) - ord('a')  
                count[char_index][size] += i - j  
                if count[char_index][size] >= 3:
                    max_length = max(max_length, size)  
                j += 1
                size += 1
        return max_length

sol = Solution()
print(sol.maximumLength("aaaa"))