
class Solution:
    def intersection(self, nums1, nums2):
        res = []
        nums1, nums2 = set(nums1), set(nums2)
        for i in nums1:
            if i not in nums2:
                res.append(i)
        return res
