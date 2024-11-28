class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        rc=Counter(ransomNote)
        mc=Counter(magazine)

        for char,count in rc.items():
            if mc[char]<count:
                return False
        return True