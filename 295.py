
class MedianFinder:
    def __init__(self):
        self.data = []

    def addNum(self, num):

        if len(self.data) == 0:
            self.data.append(num)
        elif num < self.data[0]:
            self.data.insert(0, num)
        elif num > self.data[-1]:
            self.data.append(num)
        else:
            l, r = 0, len(self.data)
            while l < r-1:
                mid = (l+r) // 2
                if self.data[mid] > num:
                    r = mid
                elif self.data[mid] < num:
                    l = mid
                else:
                    self.data.insert(mid, num)
                    return
            self.data.insert(r, num)


    def findMedian(self):

        n = len(self.data)
        status = n % 2

        if status:
            return self.data[n//2]
        else:
            return (self.data[n/2-1] + self.data[n/2]) / 2
