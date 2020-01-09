
class Solution:
    def intersect(self, nums1, nums2):
        res = []
        d1, d2 = self.frequencyStatistic(nums1), self.frequencyStatistic(nums2)
        for item in d1:
            status = min(d1[item], d2.get(item, 0))
            if status:
                for i in range(status):
                    res.append(item)
        return res

    def frequencyStatistic(self, nums):
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d.update({num:1})
        return d
