class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        hashmap={}
        for r in range(len(fruits)):
            if fruits[r] not in hashmap:
                hashmap[fruits[r]]=1
            else:
                hashmap[fruits[r]]+=1
            if len(hashmap)>2:
                hashmap[fruits[l]]-=1
                if hashmap[fruits[l]]==0:
                    hashmap.pop(fruits[l])
                l+=1
        return r-l+1

        
            
            
        

        