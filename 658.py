
class Solution:
    def findClostestElements(self, arr, k, x):
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[-k:]
        l, r = 0, len(arr)-1
        while r-l > k:
            if arr[r]-x > x-arr[l]:
                r -= 1
            elif arr[r]-x < x-arr[l]:
                l += 1
            else:
                r -= 1
                l += 1

        return arr[l:r]

