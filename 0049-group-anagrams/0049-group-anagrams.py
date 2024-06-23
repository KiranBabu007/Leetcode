class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}

        for i in strs:
            key=''.join(sorted(i))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(i)
        return list(hashmap.values())

        