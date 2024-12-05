class Solution(object):
    def romanToInt(self, s):
        roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        result = ''

        for value, symbol in roman:
            while s >= value:
                result += symbol
                s -= value

        return result

res = Solution()
print(res.romanToInt('MMV'))
        