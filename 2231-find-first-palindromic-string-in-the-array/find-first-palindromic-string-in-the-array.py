class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if i[::-1]==i:
                return i
        return ""