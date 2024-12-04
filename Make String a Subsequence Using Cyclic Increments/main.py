class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        index = 0
        s2_length = len(str2)
        for i in str1:
            if index < s2_length and (ord(str2[index]) - ord(i)) % 26 < 2:
                index += 1
        return index == s2_length
