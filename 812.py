
class Solution:
    def largestTriangleArea(self, points):
        n = len(points)
        res = 0

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    (x1,y1), (x2,y2), (x3,y3) = points[i], points[j], points[k]
                    res = max(res, abs(0.5* (x1*(y2-y3) + x2*(y3-y1) +x3*(y1-y2))))
        return res
