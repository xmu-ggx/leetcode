
class Solution:
    def merge(self,nums1, m, nums2, n):
        
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for j in range(n):
            temp = nums2[j]

            for i in range(m+n):

                if nums1[i] < temp:
                    i += 1
                else:
                    nums.insert(i,temp)

