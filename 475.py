
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        distance = [self.binarySearch(heaters, house) for house in houses]
        return max(distance)

    def binarySearch(self, ls, target):
        if target <= ls[0]:
            return ls[0] - target
        if target >= ls[-1]:
            return target - ls[-1]

        l, r = 0, len(ls)-1
        while l < r-1:
            mid = (l+r)//2
            if ls[mid] > target:
                r = mid
            elif ls[mid] < target:
                l = mid
            else:
                return 0
        return min(ls[r]-target, target-ls[l])

if __name__ == '__main__':
    test = [1,4,6,8,9]
    target = 12
    print(Solution().binarySearch(test, target))
