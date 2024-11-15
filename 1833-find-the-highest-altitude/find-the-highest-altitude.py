class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=[0]
        for i in range(len(gain)):
            alt.append(alt[i]+gain[i])
        return max(alt)
        