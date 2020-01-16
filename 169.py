
class Solution:
    def majorityElement(self, nums):
        hashtable = {}
        thres = int(len(nums)/2)
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1

        for key in hashtable:
            if hashtable[key] > thres:
                return key
