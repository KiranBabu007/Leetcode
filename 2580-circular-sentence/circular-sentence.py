class Solution(object):
    def isCircularSentence(self, sentence):
        
        l=sentence.split()

        if len(l)==1:
            return l[0][-1]==l[0][0]
            
        for i in range(len(l)):
            if l[i][-1]!=l[(i+1)%len(l)][0]:
                return False
        return True
        