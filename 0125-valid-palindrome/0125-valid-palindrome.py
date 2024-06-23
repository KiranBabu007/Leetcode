class Solution(object):
    def isPalindrome(self, s):
        str=''
        for i in s:
            if i.isalpha() or i.isnumeric():
                str+=lower(i)
        return str[::-1]==str
        