
class Solution:
    def minTimeToVisitAllPoints(self, points):
        res = 0
        for i in range(len(points)-1):
            res += self.minDistance(points[i], points[i+1])
        return res

    def minDistance(self, point1, point2):
        (x1, y1), (x2, y2) = point1, point2
        dx = abs(x1-x2)
        dy = abs(y1-y2)
        min_ = min(dx, dy)
        if min_:
            return min_ + dx-min_ + dy-min_
        else:
            return dx if dx else dy
