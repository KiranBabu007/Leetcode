class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        normal_str=''.join(char.lower() if char.isalnum() else ' ' for char in paragraph)
        words=[]
        for word in normal_str.split():
            if word not in banned:
                words.append(word)
        c=Counter(words)
        return max(c,key=c.get)