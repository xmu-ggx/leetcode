
class Solution:
    def isBoomerang(self, points):
        i = (points[1][1]-points[0][1])*(points[2][0]-points[0][0])
        j = (points[2][1]-points[0][1])*(points[1][0]-points[0][0])
        return i != j
